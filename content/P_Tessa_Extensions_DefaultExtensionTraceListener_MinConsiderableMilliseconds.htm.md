# DefaultExtensionTraceListener.MinConsiderableMilliseconds - свойство
Минимальное количество миллисекунд, которое должно выполняться расширение для
того, чтобы для него было создано сообщение трассировки, если используются
трассировщики
[ServerProfile](T_Tessa_Extensions_ExtensionTraceListenerType.htm) или
[ClientProfile](T_Tessa_Extensions_ExtensionTraceListenerType.htm). Если
значение равно 0 или отрицательное, то сообщения трассировки создаются для
всех объектов. Если значение равно null, то время выполнения расширения не
замеряется.
## __Definition
 **Пространство имён:** [Tessa.Extensions](N_Tessa_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public long? MinConsiderableMilliseconds { get; set; }
VB __Копировать
     Public Property MinConsiderableMilliseconds As Long?
    	Get
    	Set
C++ __Копировать
     public:
    property Nullable<long long> MinConsiderableMilliseconds {
    	Nullable<long long> get ();
    	void set (Nullable<long long> value);
    }
F# __Копировать
     member MinConsiderableMilliseconds : Nullable<int64> with get, set
#### Значение свойства
[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[Int64](https://learn.microsoft.com/dotnet/api/system.int64)>
##  __См. также
#### Ссылки
[DefaultExtensionTraceListener -
](T_Tessa_Extensions_DefaultExtensionTraceListener.htm)
[Tessa.Extensions - пространство имён](N_Tessa_Extensions.htm)
