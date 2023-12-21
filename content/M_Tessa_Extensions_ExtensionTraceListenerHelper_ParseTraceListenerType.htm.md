# ExtensionTraceListenerHelper.ParseTraceListenerType - метод
Возвращает режим трассировки, заданный строкой текста, или null, если
трассировка отключена.
## __Definition
 **Пространство имён:** [Tessa.Extensions](N_Tessa_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static (ExtensionTraceListenerType? listenerType, long? minConsiderableMilliseconds) ParseTraceListenerType(
    	string text,
    	bool isServer
    )
VB __Копировать
     Public Shared Function ParseTraceListenerType ( 
    	text As String,
    	isServer As Boolean
    ) As (listenerType As ExtensionTraceListenerType?, minConsiderableMilliseconds As Long?)
C++ __Копировать
     public:
    static ValueTuple<Nullable<ExtensionTraceListenerType>, Nullable<long long>> ParseTraceListenerType(
    	String^ text, 
    	bool isServer
    )
F# __Копировать
     static member ParseTraceListenerType : 
            text : string * 
            isServer : bool -> ValueTuple<Nullable<ExtensionTraceListenerType>, Nullable<int64>> 
#### Параметры
text [String](https://learn.microsoft.com/dotnet/api/system.string)
    Строка текста, определяющая режим трассировки.
isServer [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)
    true, если трассировка происходит на сервере; false, если на клиенте. 
#### Возвращаемое значение
[ValueTuple](https://learn.microsoft.com/dotnet/api/system.valuetuple-2)<[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[ExtensionTraceListenerType](T_Tessa_Extensions_ExtensionTraceListenerType.htm)>,
[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[Int64](https://learn.microsoft.com/dotnet/api/system.int64)>>  
Режим трассировки или null, если трассировка отключена.
## __См. также
#### Ссылки
[ExtensionTraceListenerHelper -
](T_Tessa_Extensions_ExtensionTraceListenerHelper.htm)
[Tessa.Extensions - пространство имён](N_Tessa_Extensions.htm)
