# ApplicationHostConnectionInfo.ConnectTimeout - свойство
Таймаут подключения к сервису или null, если используются текущие таймауты в
настройках. Применяется для указания всех таймаутов: открытие соединения,
отправка запроса, закрытие соединения.
## __Definition
 **Пространство имён:**
[Tessa.Applications.Services.TessaServer](N_Tessa_Applications_Services_TessaServer.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public TimeSpan? ConnectTimeout { get; set; }
VB __Копировать
     Public Property ConnectTimeout As TimeSpan?
    	Get
    	Set
C++ __Копировать
     public:
    property Nullable<TimeSpan> ConnectTimeout {
    	Nullable<TimeSpan> get ();
    	void set (Nullable<TimeSpan> value);
    }
F# __Копировать
     member ConnectTimeout : Nullable<TimeSpan> with get, set
#### Значение свойства
[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[TimeSpan](https://learn.microsoft.com/dotnet/api/system.timespan)>
##  __См. также
#### Ссылки
[ApplicationHostConnectionInfo -
](T_Tessa_Applications_Services_TessaServer_ApplicationHostConnectionInfo.htm)
[Tessa.Applications.Services.TessaServer - пространство
имён](N_Tessa_Applications_Services_TessaServer.htm)
