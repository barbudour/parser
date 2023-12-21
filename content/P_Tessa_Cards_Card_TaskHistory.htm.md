# Card.TaskHistory - свойство
Список с информацией по завершённым заданиям, которые были выданы на карточку.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public ListStorage<CardTaskHistoryItem> TaskHistory { get; set; }
VB __Копировать
     Public Property TaskHistory As ListStorage(Of CardTaskHistoryItem)
    	Get
    	Set
C++ __Копировать
     public:
    property ListStorage<CardTaskHistoryItem^>^ TaskHistory {
    	ListStorage<CardTaskHistoryItem^>^ get ();
    	void set (ListStorage<CardTaskHistoryItem^>^ value);
    }
F# __Копировать
     member TaskHistory : ListStorage<CardTaskHistoryItem> with get, set
#### Значение свойства
[ListStorage](T_Tessa_Platform_Storage_ListStorage_1.htm)<[CardTaskHistoryItem](T_Tessa_Cards_CardTaskHistoryItem.htm)>
##  __Заметки
Для того, чтобы обратиться к значению этого свойства, свойство карточки
[InstanceType](P_Tessa_Cards_Card_InstanceType.htm) должно быть равным
[Card](T_Tessa_Cards_CardInstanceType.htm).
## __См. также
#### Ссылки
[Card - ](T_Tessa_Cards_Card.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
