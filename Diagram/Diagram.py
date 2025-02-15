import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Create a figure and axis
fig, ax = plt.subplots(figsize=(10, 6))
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.set_xticks([])
ax.set_yticks([])
ax.set_frame_on(False)


# Function to draw entity boxes
def draw_entity(x, y, title, attributes):
    ax.add_patch(patches.Rectangle((x, y), 2.5, 1.5, fill=True, edgecolor="black", facecolor="lightblue", lw=2))
    ax.text(x + 1.25, y + 1.35, title, fontsize=12, fontweight="bold", ha="center")

    for i, attr in enumerate(attributes):
        ax.text(x + 1.25, y + 1.2 - (i * 0.2), attr, fontsize=10, ha="center")


# Draw DictionaryData entity
draw_entity(1, 6, "DictionaryData", ["syskey (PK)", "createdDate", "modifiedDate", "status", "T1 - T10", "N1 - N10"])

# Draw PhoneticsData entity
draw_entity(5, 7, "PhoneticsData",
            ["id (PK)", "dictionaryId (FK)", "text", "audio", "sourceUrl", "licenseName", "licenseUrl"])

# Draw MeaningData entity
draw_entity(5, 4, "MeaningData", ["id (PK)", "dictionaryId (FK)", "partOfSpeech", "definition", "synonyms", "antonyms"])

# Draw relationships
ax.plot([3.5, 5], [7.25, 7.25], "k-", lw=2)  # DictionaryData - PhoneticsData
ax.text(4.2, 7.4, "1", fontsize=12, fontweight="bold")
ax.text(4.8, 7.4, "M", fontsize=12, fontweight="bold")

ax.plot([3.5, 5], [6.25, 4.75], "k-", lw=2)  # DictionaryData - MeaningData
ax.text(4.2, 5.6, "1", fontsize=12, fontweight="bold")
ax.text(4.8, 5.6, "M", fontsize=12, fontweight="bold")

# Show the diagram
plt.show()
