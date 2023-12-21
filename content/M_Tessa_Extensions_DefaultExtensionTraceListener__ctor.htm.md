# DefaultExtensionTraceListener - конструктор
Создаёт экземпляр класса с указанием значений его свойств.
## __Definition
 **Пространство имён:** [Tessa.Extensions](N_Tessa_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public DefaultExtensionTraceListener(
    	ValidationKey key,
    	long? minConsiderableMilliseconds = null
    )
VB __Копировать
     Public Sub New ( 
    	key As ValidationKey,
    	Optional minConsiderableMilliseconds As Long? = Nothing
    )
C++ __Копировать
     public:
    DefaultExtensionTraceListener(
    	ValidationKey^ key, 
    	Nullable<long long> minConsiderableMilliseconds = nullptr
    )
F# __Копировать
     new : 
            key : ValidationKey * 
            ?minConsiderableMilliseconds : Nullable<int64> 
    (* Defaults:
            let _minConsiderableMilliseconds = defaultArg minConsiderableMilliseconds null
    *)
    -> DefaultExtensionTraceListener
#### Параметры
key [ValidationKey](T_Tessa_Platform_Validation_ValidationKey.htm)
    Ключ валидации, который используется для формирования сообщений трассировки. Не равен null.
minConsiderableMilliseconds
[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[Int64](https://learn.microsoft.com/dotnet/api/system.int64)>
(Optional)
     Минимальное количество миллисекунд, которое должно выполняться расширение для того, чтобы для него было создано сообщение трассировки, если используются трассировщики [ServerProfile](T_Tessa_Extensions_ExtensionTraceListenerType.htm) или [ClientProfile](T_Tessa_Extensions_ExtensionTraceListenerType.htm). Если значение равно 0 или отрицательное, то сообщения трассировки создаются для всех объектов. Если значение равно null, то время выполнения расширения не замеряется. 
## __См. также
#### Ссылки
[DefaultExtensionTraceListener -
](T_Tessa_Extensions_DefaultExtensionTraceListener.htm)
[Tessa.Extensions - пространство имён](N_Tessa_Extensions.htm)
