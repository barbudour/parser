# DefaultExtensionTraceListener.Create - метод
Создаёт объект, выполняющий отслеживание событий в соответствии с заданным
типом.
## __Definition
 **Пространство имён:** [Tessa.Extensions](N_Tessa_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static DefaultExtensionTraceListener Create(
    	ExtensionTraceListenerType listenerType,
    	long? minConsiderableMilliseconds
    )
VB __Копировать
     Public Shared Function Create ( 
    	listenerType As ExtensionTraceListenerType,
    	minConsiderableMilliseconds As Long?
    ) As DefaultExtensionTraceListener
C++ __Копировать
     public:
    static DefaultExtensionTraceListener^ Create(
    	ExtensionTraceListenerType listenerType, 
    	Nullable<long long> minConsiderableMilliseconds
    )
F# __Копировать
     static member Create : 
            listenerType : ExtensionTraceListenerType * 
            minConsiderableMilliseconds : Nullable<int64> -> DefaultExtensionTraceListener 
#### Параметры
listenerType
[ExtensionTraceListenerType](T_Tessa_Extensions_ExtensionTraceListenerType.htm)
    Тип возвращаемого объекта.
minConsiderableMilliseconds
[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[Int64](https://learn.microsoft.com/dotnet/api/system.int64)>
     Минимальное количество миллисекунд, которое должно выполняться расширение для того, чтобы для него было создано сообщение трассировки, если используются трассировщики [ServerProfile](T_Tessa_Extensions_ExtensionTraceListenerType.htm) или [ClientProfile](T_Tessa_Extensions_ExtensionTraceListenerType.htm). Если значение равно 0 или отрицательное, то сообщения трассировки создаются для всех объектов. Если значение равно null, то время выполнения расширения замеряется с интервалом по умолчанию [DefaultProfileMinConsiderableMilliseconds](F_Tessa_Extensions_DefaultExtensionTraceListener_DefaultProfileMinConsiderableMilliseconds.htm). 
#### Возвращаемое значение
[DefaultExtensionTraceListener](T_Tessa_Extensions_DefaultExtensionTraceListener.htm)  
Объект, выполняющий отслеживание событий в соответствии с заданным типом.
##  __См. также
#### Ссылки
[DefaultExtensionTraceListener -
](T_Tessa_Extensions_DefaultExtensionTraceListener.htm)
[Tessa.Extensions - пространство имён](N_Tessa_Extensions.htm)
