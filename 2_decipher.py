encoded = """
   !!junk-77!! | [3::DW::ok] | [xx::DRSC::bad] |
   [1::NFFU::ok] | ##nothing## | [5::TQI_QNGWFWD::ok] |
   [2::OG::ok] | [4::XLI::ok] | [7::WT7::bad] |
   [6::GZ_7_VS::ok] | [99::IGNORE_ME::bad] | %%noise%%
"""

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

encoded = encoded.replace("\n", "").strip()

parts = encoded.split(" | ")

decoded1 = ""
decoded2 = ""
decoded3 = ""
decoded4 = ""
decoded5 = ""
decoded6 = ""

for part in parts:
    if "[" in part and "]" in part:
        left = part.find("[")
        right = part.find("]")
        content = part[left + 1:right]

        fragment = content.split("::")
        number_str = fragment[0]
        jumbled = fragment[1]
        status = fragment[2]

        if status == "ok" and number_str.isdigit():
            shift = int(number_str)

            if shift >= 1 and shift <= 6:
                decoded = ""
                for char in jumbled:
                    if char in alphabet:
                        pos = alphabet.find(char)
                        new_pos = pos - shift
                        if new_pos < 0:
                            new_pos = new_pos + 26
                        decoded = decoded + alphabet[new_pos]
                    else:
                        decoded = decoded + char

                if shift == 1:
                    decoded1 = decoded
                elif shift == 2:
                    decoded2 = decoded
                elif shift == 3:
                    decoded3 = decoded
                elif shift == 4:
                    decoded4 = decoded
                elif shift == 5:
                    decoded5 = decoded
                elif shift == 6:
                    decoded6 = decoded

final_message = decoded1 + " " + decoded2 + " " + decoded3 + " " + decoded4 + " " + decoded5 + " " + decoded6

print(final_message)
