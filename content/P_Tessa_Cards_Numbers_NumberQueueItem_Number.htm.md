# NumberQueueItem.Number - свойство
Номер, для которого требуется выполнить действие в очереди. У номера должен
быть заполнен тип [Type](P_Tessa_Cards_Numbers_NumberStorageObject_Type.htm),
но остальные поля могут быть пустыми, если для выполнения действия
[QueueActionType](P_Tessa_Cards_Numbers_NumberQueueItem_QueueActionType.htm)
не требуется указать конкретный номер, а достаточно лишь общей информации.
## __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public NumberStorageObject Number { get; set; }
VB __Копировать
     Public Property Number As NumberStorageObject
    	Get
    	Set
C++ __Копировать
     public:
    property NumberStorageObject^ Number {
    	NumberStorageObject^ get ();
    	void set (NumberStorageObject^ value);
    }
F# __Копировать
     member Number : NumberStorageObject with get, set
#### Значение свойства
[NumberStorageObject](T_Tessa_Cards_Numbers_NumberStorageObject.htm)
##  __Заметки
Значение свойства никогда не равно null.
## __См. также
#### Ссылки
[NumberQueueItem - ](T_Tessa_Cards_Numbers_NumberQueueItem.htm)
[Tessa.Cards.Numbers - пространство имён](N_Tessa_Cards_Numbers.htm)
