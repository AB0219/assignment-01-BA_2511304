{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMGgue+xsCCb152GAlILxJn",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/AB0219/assignment-01-BA_2511304/blob/main/part1_grade_tracker.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "C52-qJ6-HGsp",
        "outputId": "60f4cb9e-a8fc-4d47-ba90-f7d3348e156c"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Ayesha Sharma → ✓ Valid name\n",
            "================================\n",
            "Student : Ayesha Sharma\n",
            "Roll No : 101\n",
            "Marks   : [88, 72, 95, 60, 78]\n",
            "================================\n",
            "Rohit Verma → ✓ Valid name\n",
            "================================\n",
            "Student : Rohit Verma\n",
            "Roll No : 102\n",
            "Marks   : [55, 68, 49, 72, 61]\n",
            "================================\n",
            "Priya Nair → ✓ Valid name\n",
            "================================\n",
            "Student : Priya Nair\n",
            "Roll No : 103\n",
            "Marks   : [91, 85, 88, 94, 79]\n",
            "================================\n",
            "Karan Mehta → ✓ Valid name\n",
            "================================\n",
            "Student : Karan Mehta\n",
            "Roll No : 104\n",
            "Marks   : [40, 55, 38, 62, 50]\n",
            "================================\n",
            "Sneha Pillai → ✓ Valid name\n",
            "================================\n",
            "Student : Sneha Pillai\n",
            "Roll No : 105\n",
            "Marks   : [75, 80, 70, 68, 85]\n",
            "================================\n",
            "\n",
            "Special Output:\n",
            "PRIYA NAIR\n",
            "priya nair\n"
          ]
        }
      ],
      "source": [
        "raw_students = [\n",
        "    {\"name\": \"  ayesha SHARMA  \", \"roll\": \"101\", \"marks_str\": \"88, 72, 95, 60, 78\"},\n",
        "    {\"name\": \"ROHIT verma\",       \"roll\": \"102\", \"marks_str\": \"55, 68, 49, 72, 61\"},\n",
        "    {\"name\": \"  Priya Nair  \",    \"roll\": \"103\", \"marks_str\": \"91, 85, 88, 94, 79\"},\n",
        "    {\"name\": \"karan MEHTA\",       \"roll\": \"104\", \"marks_str\": \"40, 55, 38, 62, 50\"},\n",
        "    {\"name\": \" Sneha pillai \",    \"roll\": \"105\", \"marks_str\": \"75, 80, 70, 68, 85\"},\n",
        "]\n",
        "\n",
        "cleaned_students = []\n",
        "\n",
        "for student in raw_students:\n",
        "    name = student[\"name\"].strip().title()\n",
        "    roll = int(student[\"roll\"])\n",
        "    marks = list(map(int, student[\"marks_str\"].split(\", \")))\n",
        "\n",
        "\n",
        "    valid = all(word.isalpha() for word in name.split())\n",
        "    print(f\"{name} → {'✓ Valid name' if valid else '✗ Invalid name'}\")\n",
        "\n",
        "    cleaned_students.append({\n",
        "        \"name\": name,\n",
        "        \"roll\": roll,\n",
        "        \"marks\": marks\n",
        "    })\n",
        "\n",
        "\n",
        "    print(\"=\" * 32)\n",
        "    print(f\"Student : {name}\")\n",
        "    print(f\"Roll No : {roll}\")\n",
        "    print(f\"Marks   : {marks}\")\n",
        "    print(\"=\" * 32)\n",
        "\n",
        "\n",
        "for s in cleaned_students:\n",
        "    if s[\"roll\"] == 103:\n",
        "        print(\"\\nSpecial Output:\")\n",
        "        print(s[\"name\"].upper())\n",
        "        print(s[\"name\"].lower())"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "student_name = \"Ayesha Sharma\"\n",
        "subjects = [\"Math\", \"Physics\", \"CS\", \"English\", \"Chemistry\"]\n",
        "marks = [88, 72, 95, 60, 78]\n",
        "\n",
        "\n",
        "for i in range(len(subjects)):\n",
        "    m = marks[i]\n",
        "\n",
        "    if m >= 90:\n",
        "        grade = \"A+\"\n",
        "    elif m >= 80:\n",
        "        grade = \"A\"\n",
        "    elif m >= 70:\n",
        "        grade = \"B\"\n",
        "    elif m >= 60:\n",
        "        grade = \"C\"\n",
        "    else:\n",
        "        grade = \"F\"\n",
        "\n",
        "    print(f\"{subjects[i]} : {m} → {grade}\")\n",
        "\n",
        "\n",
        "total = sum(marks)\n",
        "average = round(total / len(marks), 2)\n",
        "\n",
        "highest = max(marks)\n",
        "lowest = min(marks)\n",
        "\n",
        "print(\"\\nTotal:\", total)\n",
        "print(\"Average:\", average)\n",
        "print(\"Highest:\", f\"{subjects[marks.index(highest)]} -> {highest}\")\n",
        "print(\"Lowest :\", f\"{subjects[marks.index(lowest)]} -> {lowest}\")\n",
        "\n",
        "\n",
        "count = 0\n",
        "\n",
        "while True:\n",
        "    subject = input(\"Enter new subject to be added (or 'done'): \")\n",
        "\n",
        "    if subject.lower() == \"done\":\n",
        "        break\n",
        "\n",
        "    marks_input = input(\"Enter marks: \")\n",
        "\n",
        "    if not marks_input.isdigit():\n",
        "        print(\"Invalid marks!\")\n",
        "        continue\n",
        "\n",
        "    marks_value = int(marks_input)\n",
        "\n",
        "    if marks_value < 0 or marks_value > 100:\n",
        "        print(\"Marks must be between 0-100\")\n",
        "        continue\n",
        "\n",
        "    subjects.append(subject)\n",
        "    marks.append(marks_value)\n",
        "    count += 1\n",
        "\n",
        "print(\"New subjects added:\", count)\n",
        "print(\"Updated average:\", round(sum(marks)/len(marks), 2))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "RrPmxbwwwOn4",
        "outputId": "36d995a4-9e33-4ab8-b637-a6327f5f9f43"
      },
      "execution_count": 10,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Math : 88 → A\n",
            "Physics : 72 → B\n",
            "CS : 95 → A+\n",
            "English : 60 → C\n",
            "Chemistry : 78 → B\n",
            "\n",
            "Total: 393\n",
            "Average: 78.6\n",
            "Highest: CS -> 95\n",
            "Lowest : English -> 60\n",
            "Enter new subject to be added (or 'done'): play\n",
            "Enter marks: 98\n",
            "Enter new subject to be added (or 'done'): done\n",
            "New subjects added: 1\n",
            "Updated average: 81.83\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "class_data = [\n",
        "    (\"Ayesha Sharma\",  [88, 72, 95, 60, 78]),\n",
        "    (\"Rohit Verma\",    [55, 68, 49, 72, 61]),\n",
        "    (\"Priya Nair\",     [91, 85, 88, 94, 79]),\n",
        "    (\"Karan Mehta\",    [40, 55, 38, 62, 50]),\n",
        "    (\"Sneha Pillai\",   [75, 80, 70, 68, 85]),\n",
        "]\n",
        "\n",
        "print(\"Name              | Average | Status\")\n",
        "print(\"-\" * 40)\n",
        "\n",
        "pass_count = 0\n",
        "fail_count = 0\n",
        "topper = \"\"\n",
        "top_avg = 0\n",
        "total_avg = 0\n",
        "\n",
        "for name, marks in class_data:\n",
        "    avg = round(sum(marks)/len(marks), 2)\n",
        "    total_avg += avg\n",
        "\n",
        "    status = \"Pass\" if avg >= 60 else \"Fail\"\n",
        "\n",
        "    if status == \"Pass\":\n",
        "        pass_count += 1\n",
        "    else:\n",
        "        fail_count += 1\n",
        "\n",
        "    if avg > top_avg:\n",
        "        top_avg = avg\n",
        "        topper = name\n",
        "\n",
        "    print(f\"{name:<18} | {avg:^7} | {status}\")\n",
        "\n",
        "class_avg = round(total_avg / len(class_data), 2)\n",
        "\n",
        "print(\"\\nPassed:\", pass_count)\n",
        "print(\"Failed:\", fail_count)\n",
        "print(\"Topper:\", topper, top_avg)\n",
        "print(\"Class Average:\", class_avg)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "P1W9kII5zxzv",
        "outputId": "750badc2-ae1f-45e3-fa56-8c034765cff5"
      },
      "execution_count": 13,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Name              | Average | Status\n",
            "----------------------------------------\n",
            "Ayesha Sharma      |  78.6   | Pass\n",
            "Rohit Verma        |  61.0   | Pass\n",
            "Priya Nair         |  87.4   | Pass\n",
            "Karan Mehta        |  49.0   | Fail\n",
            "Sneha Pillai       |  75.6   | Pass\n",
            "\n",
            "Passed: 4\n",
            "Failed: 1\n",
            "Topper: Priya Nair 87.4\n",
            "Class Average: 70.32\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "essay = \"  python is a versatile language. it supports object oriented, functional, and procedural programming. python is widely used in data science and machine learning.  \"\n",
        "\n",
        "\n",
        "clean_essay = essay.strip()\n",
        "print(\"Clean:\", clean_essay)\n",
        "\n",
        "\n",
        "print(\"\\nTitle Case:\")\n",
        "print(clean_essay.title())\n",
        "\n",
        "\n",
        "print(\"\\nCount of 'python':\", clean_essay.count(\"python\"))\n",
        "\n",
        "\n",
        "print(\"\\nReplaced:\")\n",
        "print(clean_essay.replace(\"python\", \" 🐍\"))\n",
        "\n",
        "\n",
        "sentences = clean_essay.split(\". \")\n",
        "print(\"\\nSentence List:\", sentences)\n",
        "\n",
        "\n",
        "print(\"\\nNumbered Sentences:\")\n",
        "for i, s in enumerate(sentences, 1):\n",
        "    if not s.endswith(\".\"):\n",
        "        s += \".\"\n",
        "    print(f\"{i}. {s}\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "D_YbLcs00Ky7",
        "outputId": "0aad62c5-7586-49ee-ef07-bf4d8299a061"
      },
      "execution_count": 15,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Clean: python is a versatile language. it supports object oriented, functional, and procedural programming. python is widely used in data science and machine learning.\n",
            "\n",
            "Title Case:\n",
            "Python Is A Versatile Language. It Supports Object Oriented, Functional, And Procedural Programming. Python Is Widely Used In Data Science And Machine Learning.\n",
            "\n",
            "Count of 'python': 2\n",
            "\n",
            "Replaced:\n",
            " 🐍 is a versatile language. it supports object oriented, functional, and procedural programming.  🐍 is widely used in data science and machine learning.\n",
            "\n",
            "Sentence List: ['python is a versatile language', 'it supports object oriented, functional, and procedural programming', 'python is widely used in data science and machine learning.']\n",
            "\n",
            "Numbered Sentences:\n",
            "1. python is a versatile language.\n",
            "2. it supports object oriented, functional, and procedural programming.\n",
            "3. python is widely used in data science and machine learning.\n"
          ]
        }
      ]
    }
  ]
}