# Bioinformatics – Structural Variation Detection (Lact-FinderSV)

## 📌 Project Overview

This project focuses on the identification of structural variations in a bacterial genome through comparison with a reference genome. The analysis is performed using next-generation sequencing (NGS) data and a combination of bioinformatics tools and custom-developed scripts.

The reference genome is *Lactobacillus casei*, while the target genome (*lact.sp*) is a simulated organism containing artificial structural variations such as insertions, deletions, and inversions.

---

## 🎯 Objectives

* Align sequencing reads to a reference genome
* Analyze coverage and mapping quality
* Detect structural variations (SVs), including:

  * Long and short insertions
  * Long and short deletions
  * Inversions
* Develop custom tracks for deeper genomic analysis

---

## 🛠️ Tools & Technologies

* **BWA** – sequence alignment
* **Samtools** – SAM/BAM file processing
* **IGV (Integrative Genomics Viewer)** – visualization
* **Python** – custom track generation

---

## 📂 Project Structure

* `Code/` – Python scripts for track generation
* `Img/` – images from analysis
* `Plot IGV/` – IGV screenshots
* `Wig/` – generated track files (.wig)
---

## 📊 Analysis Performed

The project includes:

* Sequence coverage analysis
* Physical coverage analysis
* Single mate analysis
* Fragment length evaluation
* Orientation analysis
* Detection of anomalous mate pairs

Custom tracks were implemented to enhance the detection of structural variations and improve interpretability of genomic regions.

---

## 🚀 How to Run

1. Index the reference genome:

   ```
   bwa index reference.fasta
   ```
2. Align reads:

   ```
   bwa mem reference.fasta reads1.fastq reads2.fastq > output.sam
   ```
3. Convert and sort:

   ```
   samtools view -bS output.sam > output.bam
   samtools sort output.bam -o sorted.bam
   samtools index sorted.bam
   ```
4. Generate custom tracks using provided Python scripts
5. Load `.bam` and `.wig` files into IGV for visualization

---

## ⚠️ Academic Use Notice

This project was developed as part of a university assignment in Bioinformatics (LM-18 UniPD).

**It is intended for educational purposes only.**
Unauthorized copying, reuse, or submission of this work (in whole or in part) as original work for academic evaluation is strictly prohibited.

If you use or reference this project, **proper citation of the author is required**.

---

## ✍️ Author

Eleonora Signor

Master’s Degree in Computer Science University of Padua

---

## 📅 Year

2021/2022
