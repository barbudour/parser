# CardServerPermissionsProvider.SetFullPermissions(CardDeleteRequest) - метод
Устанавливает полные разрешения (токен прав доступа) для заданного запроса на
удаление карточки.
##  __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public virtual void SetFullPermissions(
    	CardDeleteRequest request
    )
VB __Копировать
     Public Overridable Sub SetFullPermissions ( 
    	request As CardDeleteRequest
    )
C++ __Копировать
     public:
    virtual void SetFullPermissions(
    	CardDeleteRequest^ request
    )
F# __Копировать
     abstract SetFullPermissions : 
            request : CardDeleteRequest -> unit 
    override SetFullPermissions : 
            request : CardDeleteRequest -> unit 
#### Параметры
request [CardDeleteRequest](T_Tessa_Cards_CardDeleteRequest.htm)
    Запрос на удаление карточки, для которого требуется установить полные разрешения.
#### Реализации
[ICardServerPermissionsProvider.SetFullPermissions(CardDeleteRequest)](M_Tessa_Cards_ICardServerPermissionsProvider_SetFullPermissions.htm)  
##  __См. также
#### Ссылки
[CardServerPermissionsProvider -
](T_Tessa_Cards_CardServerPermissionsProvider.htm)
[SetFullPermissions -
перегрузка](Overload_Tessa_Cards_CardServerPermissionsProvider_SetFullPermissions.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
