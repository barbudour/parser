# SessionHttpRequestHeader - класс
Заголовки HTTP, используемые при обращении к веб-сервисам Tessa.
## __Definition
 **Пространство имён:** [Tessa.Platform.Runtime](N_Tessa_Platform_Runtime.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static class SessionHttpRequestHeader
VB __Копировать
     Public NotInheritable Class SessionHttpRequestHeader
C++ __Копировать
     public ref class SessionHttpRequestHeader abstract sealed
F# __Копировать
     [<AbstractClassAttribute>]
    [<SealedAttribute>]
    type SessionHttpRequestHeader = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ SessionHttpRequestHeader
##  __Поля
[InstanceName](F_Tessa_Platform_Runtime_SessionHttpRequestHeader_InstanceName.htm)|
Имя экземпляра сервера, к которому выполняется обращение. Используется в
запросах к сервисам SOAP (WCF). Если заголовок задан, то используется его
значение (а не имя внутри заголовка
[Session](F_Tessa_Platform_Runtime_SessionHttpRequestHeader_Session.htm)).
Если заголовок не задан, то используется либо имя внутри заголовка
[Session](F_Tessa_Platform_Runtime_SessionHttpRequestHeader_Session.htm), либо
имя по умолчанию
[DefaultInstanceName](F_Tessa_Platform_Runtime_RuntimeHelper_DefaultInstanceName.htm),
если заголовок
[Session](F_Tessa_Platform_Runtime_SessionHttpRequestHeader_Session.htm) также
отсутствует.  
---|---  
[Session](F_Tessa_Platform_Runtime_SessionHttpRequestHeader_Session.htm)|
Сериализованный токен, описывающий сессию. Если заголовок задан, но
[InstanceName](F_Tessa_Platform_Runtime_SessionHttpRequestHeader_InstanceName.htm)
отсутствует, то имя экземпляра сервера используется из сессии, которая
сериализована в этом заголовке.  
[Version](F_Tessa_Platform_Runtime_SessionHttpRequestHeader_Version.htm)|
Версия платформы на сервере. Может быть разобран методом
[Parse(ReadOnlySpan<Char>)](https://learn.microsoft.com/dotnet/api/system.version.parse#system-
version-parse\(system-readonlyspan\(\(system-char\)\)\)). Может быть указана в
ответе на запрос при входе в систему. Используется менеджером приложений.
Версия платформы передаётся, начиная со сборки 3.6, если заголовок не указан,
то это версия более ранняя.  
## __См. также
#### Ссылки
[Tessa.Platform.Runtime - пространство имён](N_Tessa_Platform_Runtime.htm)
