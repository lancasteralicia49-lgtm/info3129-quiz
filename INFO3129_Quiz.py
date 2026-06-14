

import tkinter as tk
from tkinter import messagebox

questions = [
    
    (
        "NSM stands for:",
        ["A. Network Security Monitoring", "B. Network System Management", "C. National Security Monitoring", "D. Network Security Management"],
        "A"
    ),

    (
        "Which phase comes immediately after Collection?",
        ["A. Response", "B. Analysis", "C. Detection", "D. Recovery"],
        "C"
    ),

    (
        "Which phase comes immediately after Detection?",
        ["A. Analysis", "B. Protect", "C. Collection", "D. Recover"],
        "A"
    ),

    (
        "Which type of data provides summaries of communications?",
        ["A. Alert Data", "B. Session Data", "C. Full Content Data", "D. Statistical Data"],
        "B"
    ),

    (
        "Which type of data contains throughput and utilization information?",
        ["A. Statistical Data", "B. Session Data", "C. Alert Data", "D. Packet String Data"],
        "A"
    ),

    (
        "Which type of data contains IDS alerts?",
        ["A. Session Data", "B. Statistical Data", "C. Alert Data", "D. Packet String Data"],
        "C"
    ),

    (
        "Which type of defense focuses on adversary behavior?",
        ["A. Threat-centric", "B. Vulnerability-centric", "C. Compliance-centric", "D. Device-centric"],
        "A"
    ),

    (
        "Which type of defense focuses on patching weaknesses?",
        ["A. Threat-centric", "B. Vulnerability-centric", "C. Host-centric", "D. Intelligence-centric"],
        "B"
    ),

    (
        "Which domain includes event analysis?",
        ["A. Detect", "B. Protect", "C. Sustain", "D. Recover"],
        "A"
    ),

    (
        "Which domain includes awareness training?",
        ["A. Detect", "B. Protect", "C. Respond", "D. Sustain"],
        "B"
    ),

    (
        "Which domain includes malware analysis?",
        ["A. Detect", "B. Respond", "C. Sustain", "D. Recover"],
        "B"
    ),

    (
        "Which domain includes technology management?",
        ["A. Detect", "B. Recover", "C. Sustain", "D. Protect"],
        "C"
    ),

    (
        "Which tool is commonly used as a HIDS?",
        ["A. Snort", "B. Zeek", "C. OSSEC", "D. NetFlow"],
        "C"
    ),

    (
        "Which tool is commonly used as a NIDS?",
        ["A. OSSEC", "B. Snort", "C. AIDE", "D. Tripwire"],
        "B"
    ),

    (
        "Which type of data is the most storage intensive?",
        ["A. Statistical Data", "B. Alert Data", "C. Session Data", "D. Full Content Data"],
        "D"
    ),

    (
        "Which type of data requires the least storage?",
        ["A. Full Content Data", "B. Session Data", "C. Statistical Data", "D. Packet String Data"],
        "C"
    ),

    (
        "What is the primary goal of NSM?",
        ["A. Device management", "B. Visibility", "C. Prevention", "D. Compliance"],
        "B"
    ),

    (
        "Which approach assumes prevention will eventually fail?",
        ["A. Threat-centric", "B. Vulnerability-centric", "C. Device-centric", "D. Host-centric"],
        "A"
    ),

    (
        "Which type of data is commonly saved in PCAP files?",
        ["A. Session Data", "B. Statistical Data", "C. Full Content Data", "D. Alert Data"],
        "C"
    ),

    (
        "Which phase involves host forensics?",
        ["A. Collection", "B. Detection", "C. Analysis", "D. Protect"],
        "C"
    )

]




current_question = 0
score = 0

root = tk.Tk()
root.title("INFO-3129 Quiz")
root.geometry("700x400")



question_label = tk.Label(
    root,
    text=questions[0][0],
    font=("Arial",16)
)

question_label.pack(pady=20)


answer = tk.StringVar()

rb1 = tk.Radiobutton(
    root,
 text=questions[0][1][0],
    variable=answer,
    value="A"
)

rb2 = tk.Radiobutton(
    root,
    text=questions[0][1][1],
    variable=answer,
    value="B"
)

rb3 = tk.Radiobutton(
    root,
    text=questions[0][1][2],
    variable=answer,
    value="C"
)

rb4 = tk.Radiobutton(
    root,
    text=questions[0][1][3],
    variable=answer,
    value="D"
)



rb1.pack()
rb2.pack()
rb3.pack()
rb4.pack()


result = tk.Label(root, font=("Arial",12))
result.pack(pady=10)

result = tk.Label(
    root,
    text="",
    font=("Arial",12)
)

result.pack(pady=10)



def check_answer():
    global current_question, score

    if answer.get() == questions[current_question][2]:

        score += 1

        messagebox.showinfo(
            "Correct!",
            "Correct answer!"
        )

    else:

        messagebox.showerror(
            "Incorrect",
            f"Correct answer is {questions[current_question][2]}"
        )

    current_question += 1

    if current_question < len(questions):

        question_label.config(
            text=questions[current_question][0]
        )

        rb1.config(text=questions[current_question][1][0])
        rb2.config(text=questions[current_question][1][1])
        rb3.config(text=questions[current_question][1][2])
        rb4.config(text=questions[current_question][1][3])

        answer.set("")

    else:

        percentage = round(score / len(questions) * 100)

        messagebox.showinfo(
            "Quiz Complete",
            f"Score: {score}/{len(questions)}\nPercentage: {percentage}%"
        )

        root.destroy()



submit_button = tk.Button(
    root,
    text="Submit Answer",
    command=check_answer
)

submit_button.pack(pady=20)



result = tk.Label(root, font=("Arial", 12))
result.pack(pady=20)

root.mainloop()


