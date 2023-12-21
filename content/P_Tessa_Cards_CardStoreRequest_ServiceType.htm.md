# CardStoreRequest.ServiceType - свойство
Тип сервиса, от которого был получен текущий объект запроса. Позволяет
определить надёжность данных в запросе. При сериализации значение не
передаётся с клиента на сервер. Это свойство используется платформой, не
рекомендуется устанавливать его значение вручную.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public CardServiceType ServiceType { get; set; }
VB __Копировать
     Public Property ServiceType As CardServiceType
    	Get
    	Set
C++ __Копировать
     public:
    property CardServiceType ServiceType {
    	CardServiceType get ();
    	void set (CardServiceType value);
    }
F# __Копировать
     member ServiceType : CardServiceType with get, set
#### Значение свойства
[CardServiceType](T_Tessa_Cards_CardServiceType.htm)
##  __Заметки
Это свойство не записывается в хранилище, поэтому оно эффективно только для
текущего декоратора.
## __См. также
#### Ссылки
[CardStoreRequest - ](T_Tessa_Cards_CardStoreRequest.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
