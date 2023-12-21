# CardExtensionContext.EnableTracing - свойство
Признак того, что для текущего метода расширений разрешена запись сообщения
трассировки при включённой в системе трассировке. Установка значения равным
false позволяет запретить запись сообщения, например, для реализации метода,
которая по умолчанию не выполняет полезной работы. При отключённой сортировке
значение равно false.
## __Definition
 **Пространство имён:** [Tessa.Cards.Extensions](N_Tessa_Cards_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public bool EnableTracing { get; set; }
VB __Копировать
     Public Property EnableTracing As Boolean
    	Get
    	Set
C++ __Копировать
     public:
    virtual property bool EnableTracing {
    	bool get () sealed;
    	void set (bool value) sealed;
    }
F# __Копировать
     abstract EnableTracing : bool with get, set
    override EnableTracing : bool with get, set
#### Значение свойства
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)
#### Реализации
[ITraceableExtensionContext.EnableTracing](P_Tessa_Extensions_ITraceableExtensionContext_EnableTracing.htm)  
##  __См. также
#### Ссылки
[CardExtensionContext - ](T_Tessa_Cards_Extensions_CardExtensionContext.htm)
[Tessa.Cards.Extensions - пространство имён](N_Tessa_Cards_Extensions.htm)
