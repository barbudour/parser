# CardTypePriorityComparer.Order - свойство
Словарь, содержащий порядок сортировки типов карточек. Ключ - тип карточки.
Значение - порядок сортировки.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow](N_Tessa_Extensions_Default_Shared_Workflow.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public IReadOnlyDictionary<Guid, int> Order { get; }
VB __Копировать
     Public ReadOnly Property Order As IReadOnlyDictionary(Of Guid, Integer)
    	Get
C++ __Копировать
     public:
    virtual property IReadOnlyDictionary<Guid, int>^ Order {
    	IReadOnlyDictionary<Guid, int>^ get () sealed;
    }
F# __Копировать
     abstract Order : IReadOnlyDictionary<Guid, int> with get
    override Order : IReadOnlyDictionary<Guid, int> with get
#### Значение свойства
[IReadOnlyDictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlydictionary-2)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid),
[Int32](https://learn.microsoft.com/dotnet/api/system.int32)>
#### Реализации
[ICardTypePriorityComparer.Order](P_Tessa_Extensions_Default_Shared_Workflow_ICardTypePriorityComparer_Order.htm)  
##  __См. также
#### Ссылки
[CardTypePriorityComparer -
](T_Tessa_Extensions_Default_Shared_Workflow_CardTypePriorityComparer.htm)
[Tessa.Extensions.Default.Shared.Workflow - пространство
имён](N_Tessa_Extensions_Default_Shared_Workflow.htm)
