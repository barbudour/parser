# WebProxy.RequestFlags - перечисление
Параметры отправки запроса через прокси.
## __Definition
 **Пространство имён:** [Tessa.Platform.Runtime](N_Tessa_Platform_Runtime.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    [FlagsAttribute]
    protected enum RequestFlags
VB __Копировать
    <FlagsAttribute>
    Protected Enumeration RequestFlags
C++ __Копировать
    [FlagsAttribute]
    protected enum class RequestFlags
F# __Копировать
     [<FlagsAttribute>]
    type RequestFlags
##  __Члены
None| 0|  Запрос отправляется с параметрами по умолчанию.  
---|---|---  
IgnoreSession| 1|  Признак того, что метод должен игнорировать токен сессии,
т.е. не передавать его с запросом на сервер, даже если он присутствует в
объекте
[SessionTokenHolder](P_Tessa_Platform_Runtime_WebProxy_SessionTokenHolder.htm).  
UseCompression| 2|  Признак того, что передаваемые бинарные параметры
сжимаются по алгоритму Deflate. Игнорируется при текстовой сериализации с
указанием флага Json или TypedJson.  
Json| 4|  Использовать тип данных application/json для сериализации первого
параметра в текстовом формате Json. При этом остальные параметры игнорируются.
Типы данных .NET при передаче будут искажены в соответствии со стандартом.
Используйте TypedJson для сохранения типов.  
TypedJson| 8|  Использовать тип данных application/json для сериализации
первого параметра в текстовом формате Typed Json, который сохраняет типы
данных .NET при передаче. При этом остальные параметры игнорируются.  
PlainJsonResponse| 16|  Признак того, что ответ от сервиса с типом
application/json будет обработан как нетипизированный Json. Если флаг не
указан, то такой ответ обрабатывается как типизированный Json.  
ForceRequestStreaming| 32|  Признак того, что тело запроса передаётся без
буферизации как поток. По умолчанию потоковая передача выполняется только при
указании типа
[Stream](https://learn.microsoft.com/dotnet/api/system.io.stream) в качестве
параметра запроса.  
OmitInstanceInUri| 64|  Признак того, что при формировании запроса необходимо
не добавлять имя экземпляра сервера
[InstanceName](P_Tessa_Platform_Runtime_WebProxy_InstanceName.htm) в URI-адрес
запроса. Это необходимо для запросов к адресам, которые не являются MVC-
контроллерами TESSA, например, к адресу /hcheck.  
## __См. также
#### Ссылки
[Tessa.Platform.Runtime - пространство имён](N_Tessa_Platform_Runtime.htm)
