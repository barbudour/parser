# CardMetadataColumn.ParentRowSection - свойство
Секция, на строку которой ссылается текущая колонка, или null, если колонка не
ссылается на строку секции. Значение указывается только для комплексной
колонки, а также для физической, которая непосредственно ссылается на строку
секции.
## __Definition
 **Пространство имён:** [Tessa.Cards.Metadata](N_Tessa_Cards_Metadata.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public CardMetadataSectionReference ParentRowSection { get; set; }
VB __Копировать
     Public Property ParentRowSection As CardMetadataSectionReference
    	Get
    	Set
C++ __Копировать
     public:
    property CardMetadataSectionReference^ ParentRowSection {
    	CardMetadataSectionReference^ get ();
    	void set (CardMetadataSectionReference^ value);
    }
F# __Копировать
     member ParentRowSection : CardMetadataSectionReference with get, set
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
