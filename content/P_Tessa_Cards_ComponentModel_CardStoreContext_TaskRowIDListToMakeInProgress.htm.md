# CardStoreContext.TaskRowIDListToMakeInProgress - свойство
Список идентификаторов заданий, которые берутся в работу в процессе
сохранения. Для каждого такого задания выполняются дополнительные проверки
внутри блокировки на запись карточки.
## __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public List<Guid> TaskRowIDListToMakeInProgress { get; }
VB __Копировать
     Public ReadOnly Property TaskRowIDListToMakeInProgress As List(Of Guid)
    	Get
C++ __Копировать
     public:
    property List<Guid>^ TaskRowIDListToMakeInProgress {
    	List<Guid>^ get ();
    }
F# __Копировать
     member TaskRowIDListToMakeInProgress : List<Guid> with get
#### Значение свойства
[List](https://learn.microsoft.com/dotnet/api/system.collections.generic.list-1)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid)>
##  __См. также
#### Ссылки
[CardStoreContext - ](T_Tessa_Cards_ComponentModel_CardStoreContext.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
