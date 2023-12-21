# NumberControlRequest.StoreMode - свойство
Способ сохранения карточки. По умолчанию значение
[Update](T_Tessa_Cards_CardStoreMode.htm). Если карточка ещё ни разу не
сохранена [Insert](T_Tessa_Cards_CardStoreMode.htm), то в контексте операций с
номерами будет располагаться пустая карточка с неактуальными данными.
## __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public CardStoreMode StoreMode { get; set; }
VB __Копировать
     Public Property StoreMode As CardStoreMode
    	Get
    	Set
C++ __Копировать
     public:
    property CardStoreMode StoreMode {
    	CardStoreMode get ();
    	void set (CardStoreMode value);
    }
F# __Копировать
     member StoreMode : CardStoreMode with get, set
#### Значение свойства
[CardStoreMode](T_Tessa_Cards_CardStoreMode.htm)
##  __См. также
#### Ссылки
[NumberControlRequest - ](T_Tessa_Cards_Numbers_NumberControlRequest.htm)
[Tessa.Cards.Numbers - пространство имён](N_Tessa_Cards_Numbers.htm)
