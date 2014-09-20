# Question 1

Given two strings, reverse all the occurrences of second string in the first string.

* _Input_: Two strings
* _Output_: First string with every occurrence of second string reversed.

__Eg.__

* _Input_: `betty_botter_bought_a_bit_of_butter._the_butter_betty_botter_bought_was_a_bit_bitter`, `botter_bought`
* _Output_: `betty_thguob_rettob_a_bit_of_butter._the_butter_betty_thguob_rettob_was_a_bit_bitter`


# Question 2

Given two strings reverse, consider the second string as sequence of characters/deleimeters (partition points) and reverse each partition of the first string.

__Eg.__

* _Input_: `A_small_man_can_cast_a_very_big_shadow.`, `mtd`
* Intermediate:
    * A_s`m`all_`m`an_can_cas`t`_a_very_big_sha`d`ow.
    * s_A`m`_lla`m`sac_nac_na`t`ahs_gib_yrev_a_`d`.wo
* _Output_: `s_Am_llamsac_nac_natahs_gib_yrev_a_d.wo` 