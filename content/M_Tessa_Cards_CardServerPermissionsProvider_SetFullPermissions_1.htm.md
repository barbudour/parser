# CardServerPermissionsProvider.SetFullPermissions(CardGetFileContentRequest)
- метод
Устанавливает полные разрешения (токен прав доступа) для заданного запроса на
загрузку содержимого файла.
##  __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public virtual void SetFullPermissions(
    	CardGetFileContentRequest request
    )
VB __Копировать
     Public Overridable Sub SetFullPermissions ( 
    	request As CardGetFileContentRequest
    )
C++ __Копировать
     public:
    virtual void SetFullPermissions(
    	CardGetFileContentRequest^ request
    )
F# __Копировать
     abstract SetFullPermissions : 
            request : CardGetFileContentRequest -> unit 
    override SetFullPermissions : 
            request : CardGetFileContentRequest -> unit 
#### Параметры
request
[CardGetFileContentRequest](T_Tessa_Cards_CardGetFileContentRequest.htm)
    Запрос на загрузку содержимого файла, для которого требуется установить полные разрешения.
#### Реализации
[ICardServerPermissionsProvider.SetFullPermissions(CardGetFileContentRequest)](M_Tessa_Cards_ICardServerPermissionsProvider_SetFullPermissions_1.htm)  
##  __См. также
#### Ссылки
[CardServerPermissionsProvider -
](T_Tessa_Cards_CardServerPermissionsProvider.htm)
[SetFullPermissions -
перегрузка](Overload_Tessa_Cards_CardServerPermissionsProvider_SetFullPermissions.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
