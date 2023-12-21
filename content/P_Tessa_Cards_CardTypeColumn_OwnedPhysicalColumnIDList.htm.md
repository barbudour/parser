# CardTypeColumn.OwnedPhysicalColumnIDList - свойство
Список идентификаторов физических колонок, которые определяют значения полей
колонки в дочерней секции. Колонки указываются для секции
[OwnedSectionID](P_Tessa_Cards_CardTypeColumn_OwnedSectionID.htm).
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public SealableList<Guid> OwnedPhysicalColumnIDList { get; set; }
VB __Копировать
     Public Property OwnedPhysicalColumnIDList As SealableList(Of Guid)
    	Get
    	Set
C++ __Копировать
     public:
    property SealableList<Guid>^ OwnedPhysicalColumnIDList {
    	SealableList<Guid>^ get ();
    	void set (SealableList<Guid>^ value);
    }
F# __Копировать
     member OwnedPhysicalColumnIDList : SealableList<Guid> with get, set
#### Значение свойства
[SealableList](T_Tessa_Platform_Collections_SealableList_1.htm)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid)>
##  __Заметки
Значение свойства никогда не равно null.
## __Исключения
[Tessa.Platform.ObjectSealedException]| Произведена попытка изменения объекта,
защищённого от изменений.  
---|---  
##  __См. также
#### Ссылки
[CardTypeColumn - ](T_Tessa_Cards_CardTypeColumn.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
[Tessa.Platform.ObjectSealedException]
