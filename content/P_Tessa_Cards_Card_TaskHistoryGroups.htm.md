# Card.TaskHistoryGroups - свойство
Список с информацией по группам заданий, которые были выданы на карточку.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public ListStorage<CardTaskHistoryGroup> TaskHistoryGroups { get; set; }
VB __Копировать
     Public Property TaskHistoryGroups As ListStorage(Of CardTaskHistoryGroup)
    	Get
    	Set
C++ __Копировать
     public:
    property ListStorage<CardTaskHistoryGroup^>^ TaskHistoryGroups {
    	ListStorage<CardTaskHistoryGroup^>^ get ();
    	void set (ListStorage<CardTaskHistoryGroup^>^ value);
    }
F# __Копировать
     member TaskHistoryGroups : ListStorage<CardTaskHistoryGroup> with get, set
#### Значение свойства
[ListStorage](T_Tessa_Platform_Storage_ListStorage_1.htm)<[CardTaskHistoryGroup](T_Tessa_Cards_CardTaskHistoryGroup.htm)>
##  __Заметки
Для того, чтобы обратиться к значению этого свойства, свойство карточки
[InstanceType](P_Tessa_Cards_Card_InstanceType.htm) должно быть равным
[Card](T_Tessa_Cards_CardInstanceType.htm).
## __См. также
#### Ссылки
[Card - ](T_Tessa_Cards_Card.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
