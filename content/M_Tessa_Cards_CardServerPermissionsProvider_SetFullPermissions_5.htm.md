# CardServerPermissionsProvider.SetFullPermissions(CardStoreRequest) - метод
Устанавливает полные разрешения (токен прав доступа) для заданного запроса на
сохранение карточки.
##  __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public virtual void SetFullPermissions(
    	CardStoreRequest request
    )
VB __Копировать
     Public Overridable Sub SetFullPermissions ( 
    	request As CardStoreRequest
    )
C++ __Копировать
     public:
    virtual void SetFullPermissions(
    	CardStoreRequest^ request
    )
F# __Копировать
     abstract SetFullPermissions : 
            request : CardStoreRequest -> unit 
    override SetFullPermissions : 
            request : CardStoreRequest -> unit 
#### Параметры
request [CardStoreRequest](T_Tessa_Cards_CardStoreRequest.htm)
    Запрос на сохранение карточки, для которого требуется установить полные разрешения.
#### Реализации
[ICardServerPermissionsProvider.SetFullPermissions(CardStoreRequest)](M_Tessa_Cards_ICardServerPermissionsProvider_SetFullPermissions_5.htm)  
##  __См. также
#### Ссылки
[CardServerPermissionsProvider -
](T_Tessa_Cards_CardServerPermissionsProvider.htm)
[SetFullPermissions -
перегрузка](Overload_Tessa_Cards_CardServerPermissionsProvider_SetFullPermissions.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
