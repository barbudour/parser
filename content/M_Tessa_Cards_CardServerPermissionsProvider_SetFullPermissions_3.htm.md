# CardServerPermissionsProvider.SetFullPermissions(CardGetRequest) - метод
Устанавливает полные разрешения (токен прав доступа) для заданного запроса на
загрузку карточки.
##  __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public virtual void SetFullPermissions(
    	CardGetRequest request
    )
VB __Копировать
     Public Overridable Sub SetFullPermissions ( 
    	request As CardGetRequest
    )
C++ __Копировать
     public:
    virtual void SetFullPermissions(
    	CardGetRequest^ request
    )
F# __Копировать
     abstract SetFullPermissions : 
            request : CardGetRequest -> unit 
    override SetFullPermissions : 
            request : CardGetRequest -> unit 
#### Параметры
request [CardGetRequest](T_Tessa_Cards_CardGetRequest.htm)
    Запрос на загрузку карточки, для которого требуется установить полные разрешения.
#### Реализации
[ICardServerPermissionsProvider.SetFullPermissions(CardGetRequest)](M_Tessa_Cards_ICardServerPermissionsProvider_SetFullPermissions_3.htm)  
##  __См. также
#### Ссылки
[CardServerPermissionsProvider -
](T_Tessa_Cards_CardServerPermissionsProvider.htm)
[SetFullPermissions -
перегрузка](Overload_Tessa_Cards_CardServerPermissionsProvider_SetFullPermissions.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
