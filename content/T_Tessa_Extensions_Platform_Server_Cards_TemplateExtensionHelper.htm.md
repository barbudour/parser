# TemplateExtensionHelper - класс
Вспомогательные методы и константы для расширений на карточки шаблонов.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Server.Cards](N_Tessa_Extensions_Platform_Server_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static class TemplateExtensionHelper
VB __Копировать
     Public NotInheritable Class TemplateExtensionHelper
C++ __Копировать
     public ref class TemplateExtensionHelper abstract sealed
F# __Копировать
     [<AbstractClassAttribute>]
    [<SealedAttribute>]
    type TemplateExtensionHelper = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ TemplateExtensionHelper
##  __Методы
[GetVirtualCardDigest](M_Tessa_Extensions_Platform_Server_Cards_TemplateExtensionHelper_GetVirtualCardDigest.htm)|
Возвращает отображаемый Digest карточки, из которой был создан шаблон.  
---|---  
[HasEditPermissionsAsync](M_Tessa_Extensions_Platform_Server_Cards_TemplateExtensionHelper_HasEditPermissionsAsync.htm)|
Возвращает признак того, что заданный пользователь имеет права на
редактирование и удаление шаблона с заданным идентификатором.  
[HasOpenPermissionsAsync](M_Tessa_Extensions_Platform_Server_Cards_TemplateExtensionHelper_HasOpenPermissionsAsync.htm)|
Возвращает признак того, что заданный пользователь имеет права на открытие
шаблона и создания карточки из шаблона с заданным идентификатором.  
[IsAvailableForTemplateRoleAsync](M_Tessa_Extensions_Platform_Server_Cards_TemplateExtensionHelper_IsAvailableForTemplateRoleAsync.htm)|
Возвращает признак того, что роль с заданным идентификатором подходит для
использования в карточке шаблона в списке ролей для задания прав на карточку.  
[SetTemplatePermissions](M_Tessa_Extensions_Platform_Server_Cards_TemplateExtensionHelper_SetTemplatePermissions.htm)|
Устанавливает разрешения для карточки шаблона.  
## __Поля
[StoreSourceKey](F_Tessa_Extensions_Platform_Server_Cards_TemplateExtensionHelper_StoreSourceKey.htm)|
Идентификатор источника для сохранения файла шаблона. Записывается в хранилище
объекта [CardFile](T_Tessa_Cards_CardFile.htm).  
---|---  
## __См. также
#### Ссылки
[Tessa.Extensions.Platform.Server.Cards - пространство
имён](N_Tessa_Extensions_Platform_Server_Cards.htm)
