# CardMetadataSection.Columns - свойство
Колонки секции.
## __Definition
 **Пространство имён:** [Tessa.Cards.Metadata](N_Tessa_Cards_Metadata.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public CardMetadataColumnCollection Columns { get; set; }
VB __Копировать
     Public Property Columns As CardMetadataColumnCollection
    	Get
    	Set
C++ __Копировать
     public:
    property CardMetadataColumnCollection^ Columns {
    	CardMetadataColumnCollection^ get ();
    	void set (CardMetadataColumnCollection^ value);
    }
F# __Копировать
     member Columns : CardMetadataColumnCollection with get, set
#### Значение свойства
[CardMetadataColumnCollection](T_Tessa_Cards_Metadata_CardMetadataColumnCollection.htm)
##  __Заметки
Значение свойства никогда не равно null.
## __Исключения
[Tessa.Platform.ObjectSealedException]| Произведена попытка изменения объекта,
защищённого от изменений.  
---|---  
##  __См. также
#### Ссылки
[CardMetadataSection - ](T_Tessa_Cards_Metadata_CardMetadataSection.htm)
[Tessa.Cards.Metadata - пространство имён](N_Tessa_Cards_Metadata.htm)
[Tessa.Platform.ObjectSealedException]
