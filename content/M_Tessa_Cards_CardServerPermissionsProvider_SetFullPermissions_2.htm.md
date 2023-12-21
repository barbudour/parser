# CardServerPermissionsProvider.SetFullPermissions(CardGetFileVersionsRequest)
- метод
Устанавливает полные разрешения (токен прав доступа) для заданного запроса на
загрузку версий файла.
##  __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public virtual void SetFullPermissions(
    	CardGetFileVersionsRequest request
    )
VB __Копировать
     Public Overridable Sub SetFullPermissions ( 
    	request As CardGetFileVersionsRequest
    )
C++ __Копировать
     public:
    virtual void SetFullPermissions(
    	CardGetFileVersionsRequest^ request
    )
F# __Копировать
     abstract SetFullPermissions : 
            request : CardGetFileVersionsRequest -> unit 
    override SetFullPermissions : 
            request : CardGetFileVersionsRequest -> unit 
#### Параметры
request
[CardGetFileVersionsRequest](T_Tessa_Cards_CardGetFileVersionsRequest.htm)
    Запрос на загрузку версий файла, для которого требуется установить полные разрешения.
#### Реализации
[ICardServerPermissionsProvider.SetFullPermissions(CardGetFileVersionsRequest)](M_Tessa_Cards_ICardServerPermissionsProvider_SetFullPermissions_2.htm)  
##  __См. также
#### Ссылки
[CardServerPermissionsProvider -
](T_Tessa_Cards_CardServerPermissionsProvider.htm)
[SetFullPermissions -
перегрузка](Overload_Tessa_Cards_CardServerPermissionsProvider_SetFullPermissions.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
