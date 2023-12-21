# CardMetadataSection.SectionTableType - свойство
Тип таблицы, указываемый в свойстве секции
[TableType](P_Tessa_Cards_CardSection_TableType.htm). Зависит от свойств
[SectionType](P_Tessa_Cards_Metadata_CardMetadataSection_SectionType.htm) и
[TableType](P_Tessa_Cards_Metadata_CardMetadataSection_TableType.htm). При
изменении значения этого свойства будут также изменены оба зависимых свойства,
причём значение [Unspecified](T_Tessa_Cards_CardTableType.htm) недопустимо в
качестве устанавливаемого.
## __Definition
 **Пространство имён:** [Tessa.Cards.Metadata](N_Tessa_Cards_Metadata.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public CardTableType SectionTableType { get; set; }
VB __Копировать
     Public Property SectionTableType As CardTableType
    	Get
    	Set
C++ __Копировать
     public:
    property CardTableType SectionTableType {
    	CardTableType get ();
    	void set (CardTableType value);
    }
F# __Копировать
     member SectionTableType : CardTableType with get, set
#### Значение свойства
[CardTableType](T_Tessa_Cards_CardTableType.htm)
##  __Исключения
[Tessa.Platform.ObjectSealedException]| Произведена попытка изменения объекта,
защищённого от изменений.  
---|---  
##  __См. также
#### Ссылки
[CardMetadataSection - ](T_Tessa_Cards_Metadata_CardMetadataSection.htm)
[Tessa.Cards.Metadata - пространство имён](N_Tessa_Cards_Metadata.htm)
[Tessa.Platform.ObjectSealedException]
