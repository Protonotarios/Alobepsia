# Alobepsia
Το πρόγραμμα δίνει μια λύση στο δεύτερο σκέλος του διαγωνισμού εύρεσης κατοπτρικών *αλωβηψίων* του Σαραντάκου με τη χρήση λεξικού. Περισσότερα για το πρόβλημα [εδώ](https://sarantakos.wordpress.com/2017/02/10/atbash).

Για την υλοποίηση χρησιμοποιήθηκε το ελεύθερο λεξικό [OpenOffice Greek Dictionary v0.9](http://www.elspell.gr/) ή *elspell* που δημιουργήθηκε από τον Ευριπίδη Παπακώστα και τον Steve Σταυρόπουλο και διανέμεται κάτω από τις άδειες χρήσης GPL/MPL/LGPL. Δυστυχώς είναι το μόνο ελεύθερο ελληνικό λεξικό που φαίνεται να κυκλοφορεί εκεί έξω και έτσι είναι αυτό που χρησιμοποιείται σε όλα τα λογισμικά ανοικτού κώδικα Open Office, Libre Office, Firefox κλπ.

## Χρήση

Το πρόγραμμα απαιτεί [Python 3.x](https://www.python.org/downloads/).

1. [Κατεβάστε το πρόγραμμα](https://github.com/Protonotarios/Alobepsia/releases/) και αποσυμπιέστε το.
2. Κατεβάστε το παραπάνω λεξικό και αποσυμπιέστε το, ή μπορείτε να χρησιμοποιήσετε δικά σας λεξικά.
3. Βάλτε τα αρχεία με τα λεξικά στον ίδιο φάκελο με το πρόγραμμα
4. Ανοίξτε με ένα σημειωματάριο το πρόγραμμα και ενημερώστε τη λίστα λεξικών με τα ονόματα αρχείων των λεξικών που θέλετε να χρησιμοποιήσετε.
```python
lexica = ['el_GR.dic','άλλολεξικό,txt']
``` 

## Αναφορές

Το πρόγραμμα βασίστηκε στον [κώδικα](https://sarantakos.wordpress.com/2017/02/10/atbash/#comment-413939) του χρήστη [Stazybο Hοrn](https://malvumaldit.wordpress.com/) που με τη σειρά του βασίστηκε στον [κώδικα](https://sarantakos.wordpress.com/2017/02/10/atbash/#comment-413901) του χρήστη Avonidas.

## Αποτελέσματα

Με το συγκεκριμένο λεξικό το πρόγραμμα έβγαλε τα ακόλουθα *κατοπτρικά αλωβήψια*:
```
αρθώ
ευ
κνησμό
πι
πιπί
ωά
ύμνε
ώα
```

## Σκέψεις

Θα ήταν ενδιαφέρον να χρησιμοποιηθεί ένα πιο πλούσιο λεξικό, ή ακόμα καλύτερα να δημιουργηθεί ένα με εξόρυξη λέξεων από τα άπειρα κείμενα που υπάρχουν στο Διαδίκτυο, ξεκινώντας ίσως από τη Βικιπαίδεια όπου και ελεύθερη είναι αλλά και έχει σαφώς μικρότερο αριθμό πιθανών ορθογραφικών λαθών από άλλους ιστοτόπους. Δεν ξέρω βέβαια πόσο πλούσιο λεξιλόγιο μπορεί να έχει σε σχέση ας πούμε με ένα λογοτεχνικό ιστότοπο.

Μια άλλη σκέψη πιο βατή και άμεση είναι η επέκταση του προγράμματος ώστε να δουλεύει και στα Αγγλικά. Εδώ ευτυχώς υπάρχουν πάρα πολλά έτοιμα λεξικά.

Επίσης άλλη ιδέα θα ήταν να προστεθούν κι άλλα *λογολογικά* προβλήματα. Το όνομα του προγράμματος βέβαια θα παραμείνει έτσι, αν δεν έχει βέβαια αντίρρηση ο Νίκος Σαραντάκος.

Όποιος θέλει να συνεισφέρει ας μην διστάσει να στείλει pull request με τις αλλαγές του.

Ιωάννης Πρωτονοτάριος
Φεβρουάριος 2017
