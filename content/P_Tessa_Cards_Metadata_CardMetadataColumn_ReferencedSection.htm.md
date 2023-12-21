# CardMetadataColumn.ReferencedSection - свойство
Секция, на которую ссылается комплексная колонка, или null, если колонка
является физической.
## __Definition
 **Пространство имён:** [Tessa.Cards.Metadata](N_Tessa_Cards_Metadata.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public CardMetadataSectionReference ReferencedSection { get; set; }
VB __Копировать
     Public Property ReferencedSection As CardMetadataSectionReference
    	Get
    	Set
C++ __Копировать
     public:
    property CardMetadataSectionReference^ ReferencedSection {
    	CardMetadataSectionReference^ get ();
    	void set (CardMetadataSectionReference^ value);
    }
F# __Копировать
     member ReferencedSection : CardMetadataSectionReference with get, set
#### Значение свойства
[CardMetadataSectionReference](T_Tessa_Cards_Metadata_CardMetadataSectionReference.htm)
##  __Исключения
[Tessa.Platform.ObjectSealedException]| Произведена попытка изменения объекта,
защищённого от изменений.  
---|---  
##  __См. также
#### Ссылки
[CardMetadataColumn - ](T_Tessa_Cards_Metadata_CardMetadataColumn.htm)
[Tessa.Cards.Metadata - пространство имён](N_Tessa_Cards_Metadata.htm)
[Tessa.Platform.ObjectSealedException]
