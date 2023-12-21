# ITraceableExtensionContext.EnableTracing - свойство
Признак того, что для текущего метода расширений разрешена запись сообщения
трассировки при включённой в системе трассировке. Установка значения равным
false позволяет запретить запись сообщения, например, для реализации метода,
которая по умолчанию не выполняет полезной работы. При отключённой сортировке
значение равно false.
## __Definition
 **Пространство имён:** [Tessa.Extensions](N_Tessa_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     bool EnableTracing { get; set; }
VB __Копировать
     Property EnableTracing As Boolean
    	Get
    	Set
C++ __Копировать
    property bool EnableTracing {
    	bool get ();
    	void set (bool value);
    }
F# __Копировать
     abstract EnableTracing : bool with get, set
#### Значение свойства
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)
##  __См. также
#### Ссылки
[ITraceableExtensionContext -
](T_Tessa_Extensions_ITraceableExtensionContext.htm)
[Tessa.Extensions - пространство имён](N_Tessa_Extensions.htm)
