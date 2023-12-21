# LinkHelper - класс
Вспомогательные методы для построения ссылок для клиентских и административных
приложений Tessa.
## __Definition
 **Пространство имён:** [Tessa.Platform](N_Tessa_Platform.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static class LinkHelper
VB __Копировать
     Public NotInheritable Class LinkHelper
C++ __Копировать
     public ref class LinkHelper abstract sealed
F# __Копировать
     [<AbstractClassAttribute>]
    [<SealedAttribute>]
    type LinkHelper = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ LinkHelper
##  __Методы
[GetClientLink(ISession, String,
String)](M_Tessa_Platform_LinkHelper_GetClientLink_6.htm)|  Возвращает ссылку
для клиентского приложения.  
---|---  
[GetClientLink(ISession, String, IEnumerable<KeyValuePair<String, Object>>,
String)](M_Tessa_Platform_LinkHelper_GetClientLink_4.htm)|  Возвращает ссылку
для клиентского приложения.  
[GetClientLink(ISession, String, KeyValuePair<String, Object>,
String)](M_Tessa_Platform_LinkHelper_GetClientLink_5.htm)|  Возвращает ссылку
для клиентского приложения.  
[GetClientLink(String, String, String,
String)](M_Tessa_Platform_LinkHelper_GetClientLink_2.htm)|  Возвращает ссылку
для клиентского приложения.  
[GetClientLink(ISession, String, String, Object,
String)](M_Tessa_Platform_LinkHelper_GetClientLink_7.htm)|  Возвращает ссылку
для клиентского приложения.  
[GetClientLink(String, String, String, IEnumerable<KeyValuePair<String,
Object>>, String)](M_Tessa_Platform_LinkHelper_GetClientLink.htm)|  Возвращает
ссылку для клиентского приложения.  
[GetClientLink(String, String, String, KeyValuePair<String, Object>,
String)](M_Tessa_Platform_LinkHelper_GetClientLink_1.htm)|  Возвращает ссылку
для клиентского приложения.  
[GetClientLink(String, String, String, String, Object,
String)](M_Tessa_Platform_LinkHelper_GetClientLink_3.htm)|  Возвращает ссылку
для клиентского приложения.  
[NormalizeWebAddress](M_Tessa_Platform_LinkHelper_NormalizeWebAddress.htm)|
Возвращает нормализованную ссылку на базовый адрес веб-клиента или null, если
ссылка отсутствует. По правилам нормализации из строки удаляются лишние
пробелы по краям. Если строка состояла только из пробелов, была пустой или
null, то возвращается null. Результирующая строка заканчивается на символ /
Если в строке не указан протокол, то к началу строки дописывается http://
Повторная нормализация не изменяет ссылку.  
[TryGetAction](M_Tessa_Platform_LinkHelper_TryGetAction.htm)|  Выполняет
попытку прочитать действие с приложением по параметрам, полученных по ссылке.  
## __Поля
[DeskiMobileProtocol](F_Tessa_Platform_LinkHelper_DeskiMobileProtocol.htm)|
Протокол для ссылок, предназначенных для deskiMobile.  
---|---  
[TessaAdminApplicationAlias](F_Tessa_Platform_LinkHelper_TessaAdminApplicationAlias.htm)|
Алиас приложения TessaAdmin.  
[TessaClientApplicationAlias](F_Tessa_Platform_LinkHelper_TessaClientApplicationAlias.htm)|
Алиас приложения TessaClient.  
[TessaProtocol](F_Tessa_Platform_LinkHelper_TessaProtocol.htm)|  Протокол для
ссылок, предназначенных для desktop-клиента.  
## __См. также
#### Ссылки
[Tessa.Platform - пространство имён](N_Tessa_Platform.htm)
