# CardServerPermissionsProvider.SetFullPermissions(CardNewRequest) - метод
Устанавливает полные разрешения (токен прав доступа) для заданного запроса на
создание карточки.
##  __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public virtual void SetFullPermissions(
    	CardNewRequest request
    )
VB __Копировать
     Public Overridable Sub SetFullPermissions ( 
    	request As CardNewRequest
    )
C++ __Копировать
     public:
    virtual void SetFullPermissions(
    	CardNewRequest^ request
    )
F# __Копировать
     abstract SetFullPermissions : 
            request : CardNewRequest -> unit 
    override SetFullPermissions : 
            request : CardNewRequest -> unit 
#### Параметры
request [CardNewRequest](T_Tessa_Cards_CardNewRequest.htm)
    Запрос на создание карточки, для которого требуется установить полные разрешения.
#### Реализации
[ICardServerPermissionsProvider.SetFullPermissions(CardNewRequest)](M_Tessa_Cards_ICardServerPermissionsProvider_SetFullPermissions_4.htm)  
##  __См. также
#### Ссылки
[CardServerPermissionsProvider -
](T_Tessa_Cards_CardServerPermissionsProvider.htm)
[SetFullPermissions -
перегрузка](Overload_Tessa_Cards_CardServerPermissionsProvider_SetFullPermissions.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
