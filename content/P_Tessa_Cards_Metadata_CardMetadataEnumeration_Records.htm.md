# CardMetadataEnumeration.Records - свойство
Колонки перечисления.
## __Definition
 **Пространство имён:** [Tessa.Cards.Metadata](N_Tessa_Cards_Metadata.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public SealableObjectList<CardMetadataRecord> Records { get; set; }
VB __Копировать
     Public Property Records As SealableObjectList(Of CardMetadataRecord)
    	Get
    	Set
C++ __Копировать
     public:
    property SealableObjectList<CardMetadataRecord^>^ Records {
    	SealableObjectList<CardMetadataRecord^>^ get ();
    	void set (SealableObjectList<CardMetadataRecord^>^ value);
    }
F# __Копировать
     member Records : SealableObjectList<CardMetadataRecord> with get, set
#### Значение свойства
[SealableObjectList](T_Tessa_Platform_Collections_SealableObjectList_1.htm)<[CardMetadataRecord](T_Tessa_Cards_Metadata_CardMetadataRecord.htm)>
##  __Заметки
Значение свойства никогда не равно null.
## __Исключения
[Tessa.Platform.ObjectSealedException]| Произведена попытка изменения объекта,
защищённого от изменений.  
---|---  
##  __См. также
#### Ссылки
[CardMetadataEnumeration -
](T_Tessa_Cards_Metadata_CardMetadataEnumeration.htm)
[Tessa.Cards.Metadata - пространство имён](N_Tessa_Cards_Metadata.htm)
[Tessa.Platform.ObjectSealedException]
