# ICardServerPermissionsProvider - интерфейс
Объект, предоставляющий права доступа в соответствии с активной системой прав.
Например, для типового решения предоставляет токен KrToken с полным набором
прав.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface ICardServerPermissionsProvider
VB __Копировать
     Public Interface ICardServerPermissionsProvider
C++ __Копировать
     public interface class ICardServerPermissionsProvider
F# __Копировать
     type ICardServerPermissionsProvider = interface end
##  __Методы
[SetFullPermissions(CardDeleteRequest)](M_Tessa_Cards_ICardServerPermissionsProvider_SetFullPermissions.htm)|
Устанавливает полные разрешения (токен прав доступа) для заданного запроса на
удаление карточки.  
---|---  
[SetFullPermissions(CardGetFileContentRequest)](M_Tessa_Cards_ICardServerPermissionsProvider_SetFullPermissions_1.htm)|
Устанавливает полные разрешения (токен прав доступа) для заданного запроса на
загрузку содержимого файла.  
[SetFullPermissions(CardGetFileVersionsRequest)](M_Tessa_Cards_ICardServerPermissionsProvider_SetFullPermissions_2.htm)|
Устанавливает полные разрешения (токен прав доступа) для заданного запроса на
загрузку версий файла.  
[SetFullPermissions(CardGetRequest)](M_Tessa_Cards_ICardServerPermissionsProvider_SetFullPermissions_3.htm)|
Устанавливает полные разрешения (токен прав доступа) для заданного запроса на
загрузку карточки.  
[SetFullPermissions(CardNewRequest)](M_Tessa_Cards_ICardServerPermissionsProvider_SetFullPermissions_4.htm)|
Устанавливает полные разрешения (токен прав доступа) для заданного запроса на
создание карточки.  
[SetFullPermissions(CardStoreRequest)](M_Tessa_Cards_ICardServerPermissionsProvider_SetFullPermissions_5.htm)|
Устанавливает полные разрешения (токен прав доступа) для заданного запроса на
сохранение карточки.  
##  __См. также
#### Ссылки
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
