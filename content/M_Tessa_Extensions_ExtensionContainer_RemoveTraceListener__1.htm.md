# ExtensionContainer.RemoveTraceListener<TExtension> \- метод
Удаляет регистрацию объекта, выполняющего отслеживание событий, происходящих
при выполнении расширений заданного типа.
## __Definition
 **Пространство имён:** [Tessa.Extensions](N_Tessa_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public bool RemoveTraceListener<TExtension>()
    where TExtension : class, IExtension
VB __Копировать
     Public Function RemoveTraceListener(Of TExtension As {Class, IExtension}) As Boolean
C++ __Копировать
     public:
    generic<typename TExtension>
    where TExtension : ref class, IExtension
    virtual bool RemoveTraceListener() sealed
F# __Копировать
     abstract RemoveTraceListener : unit -> bool  when 'TExtension : not struct and IExtension
    override RemoveTraceListener : unit -> bool  when 'TExtension : not struct and IExtension
#### Параметры типа
TExtension
    Тип расширений, для которого удаляется регистрация объекта.
#### Возвращаемое значение
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)  
true, если регистрация объекта была найдена и удалена; false, если регистрация
объекта отсутствовала и не была удалена.
#### Реализации
[IExtensionContainer.RemoveTraceListener<TExtension>()](M_Tessa_Extensions_IExtensionContainer_RemoveTraceListener__1.htm)  
##  __См. также
#### Ссылки
[ExtensionContainer - ](T_Tessa_Extensions_ExtensionContainer.htm)
[Tessa.Extensions - пространство имён](N_Tessa_Extensions.htm)
