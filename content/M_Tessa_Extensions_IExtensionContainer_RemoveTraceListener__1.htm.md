# IExtensionContainer.RemoveTraceListener<TExtension> \- метод
Удаляет регистрацию объекта, выполняющего отслеживание событий, происходящих
при выполнении расширений заданного типа.
## __Definition
 **Пространство имён:** [Tessa.Extensions](N_Tessa_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     bool RemoveTraceListener<TExtension>()
    where TExtension : class, IExtension
VB __Копировать
     Function RemoveTraceListener(Of TExtension As {Class, IExtension}) As Boolean
C++ __Копировать
    generic<typename TExtension>
    where TExtension : ref class, IExtension
    bool RemoveTraceListener()
F# __Копировать
     abstract RemoveTraceListener : unit -> bool  when 'TExtension : not struct and IExtension
#### Параметры типа
TExtension
    Тип расширений, для которого удаляется регистрация объекта.
#### Возвращаемое значение
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)  
true, если регистрация объекта была найдена и удалена; false, если регистрация
объекта отсутствовала и не была удалена.
## __См. также
#### Ссылки
[IExtensionContainer - ](T_Tessa_Extensions_IExtensionContainer.htm)
[Tessa.Extensions - пространство имён](N_Tessa_Extensions.htm)
