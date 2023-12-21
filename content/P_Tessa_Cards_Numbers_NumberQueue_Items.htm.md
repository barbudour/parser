# NumberQueue.Items - свойство
Список действий с номерами в порядке их поступления. Эти действия были
отложены для выполнения на сервере.
## __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public ListStorage<NumberQueueItem> Items { get; set; }
VB __Копировать
     Public Property Items As ListStorage(Of NumberQueueItem)
    	Get
    	Set
C++ __Копировать
     public:
    property ListStorage<NumberQueueItem^>^ Items {
    	ListStorage<NumberQueueItem^>^ get ();
    	void set (ListStorage<NumberQueueItem^>^ value);
    }
F# __Копировать
     member Items : ListStorage<NumberQueueItem> with get, set
#### Значение свойства
[ListStorage](T_Tessa_Platform_Storage_ListStorage_1.htm)<[NumberQueueItem](T_Tessa_Cards_Numbers_NumberQueueItem.htm)>
##  __См. также
#### Ссылки
[NumberQueue - ](T_Tessa_Cards_Numbers_NumberQueue.htm)
[Tessa.Cards.Numbers - пространство имён](N_Tessa_Cards_Numbers.htm)
