# INumberContext.TransactionMode - свойство
Получает или задаёт способ выполнения запросов, связанных с номерами.
## __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    NumberTransactionMode TransactionMode { get; set; }
VB __Копировать
     Property TransactionMode As NumberTransactionMode
    	Get
    	Set
C++ __Копировать
    property NumberTransactionMode TransactionMode {
    	NumberTransactionMode get ();
    	void set (NumberTransactionMode value);
    }
F# __Копировать
     abstract TransactionMode : NumberTransactionMode with get, set
#### Значение свойства
[NumberTransactionMode](T_Tessa_Cards_Numbers_NumberTransactionMode.htm)
##  __Исключения
[Tessa.Platform.ObjectSealedException]| Произведена попытка изменения объекта,
защищённого от изменений.  
---|---  
##  __См. также
#### Ссылки
[INumberContext - ](T_Tessa_Cards_Numbers_INumberContext.htm)
[Tessa.Cards.Numbers - пространство имён](N_Tessa_Cards_Numbers.htm)
[Tessa.Platform.ObjectSealedException]
