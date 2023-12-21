# NumberContext.TransactionMode - свойство
Получает или задаёт способ выполнения запросов, связанных с номерами.
## __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public NumberTransactionMode TransactionMode { get; set; }
VB __Копировать
     Public Property TransactionMode As NumberTransactionMode
    	Get
    	Set
C++ __Копировать
     public:
    virtual property NumberTransactionMode TransactionMode {
    	NumberTransactionMode get () sealed;
    	void set (NumberTransactionMode value) sealed;
    }
F# __Копировать
     abstract TransactionMode : NumberTransactionMode with get, set
    override TransactionMode : NumberTransactionMode with get, set
#### Значение свойства
[NumberTransactionMode](T_Tessa_Cards_Numbers_NumberTransactionMode.htm)
#### Реализации
[INumberContext.TransactionMode](P_Tessa_Cards_Numbers_INumberContext_TransactionMode.htm)  
##  __Исключения
[Tessa.Platform.ObjectSealedException]| Произведена попытка изменения объекта,
защищённого от изменений.  
---|---  
##  __См. также
#### Ссылки
[NumberContext - ](T_Tessa_Cards_Numbers_NumberContext.htm)
[Tessa.Cards.Numbers - пространство имён](N_Tessa_Cards_Numbers.htm)
[Tessa.Platform.ObjectSealedException]
