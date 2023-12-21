# Card.Tasks - свойство
Список заданий, которые были выданы на карточку и ещё не были завершены.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public ListStorage<CardTask> Tasks { get; set; }
VB __Копировать
     Public Property Tasks As ListStorage(Of CardTask)
    	Get
    	Set
C++ __Копировать
     public:
    property ListStorage<CardTask^>^ Tasks {
    	ListStorage<CardTask^>^ get ();
    	void set (ListStorage<CardTask^>^ value);
    }
F# __Копировать
     member Tasks : ListStorage<CardTask> with get, set
#### Значение свойства
[ListStorage](T_Tessa_Platform_Storage_ListStorage_1.htm)<[CardTask](T_Tessa_Cards_CardTask.htm)>
##  __Заметки
Для того, чтобы обратиться к значению этого свойства, свойство карточки
[InstanceType](P_Tessa_Cards_Card_InstanceType.htm) должно быть равным
[Card](T_Tessa_Cards_CardInstanceType.htm).
## __См. также
#### Ссылки
[Card - ](T_Tessa_Cards_Card.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
