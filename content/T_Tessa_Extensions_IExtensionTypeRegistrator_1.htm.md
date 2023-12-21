# IExtensionTypeRegistrator<TExtension> \- интерфейс
Объект, выполняющий регистрацию типа расширения в контейнере
[IExtensionContainer](T_Tessa_Extensions_IExtensionContainer.htm). Все методы
объекта являются потокобезопасными.
## __Definition
 **Пространство имён:** [Tessa.Extensions](N_Tessa_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IExtensionTypeRegistrator<TExtension>
    where TExtension : class, IExtension
VB __Копировать
     Public Interface IExtensionTypeRegistrator(Of TExtension As {Class, IExtension})
C++ __Копировать
    generic<typename TExtension>
    where TExtension : ref class, IExtension
    public interface class IExtensionTypeRegistrator
F# __Копировать
     type IExtensionTypeRegistrator<'TExtension when 'TExtension : not struct and IExtension> = interface end
#### Параметры типа
TExtension
    Тип расширения, регистрацию которого выполняется объект.
##  __Методы
[MethodAsync<TContext>](M_Tessa_Extensions_IExtensionTypeRegistrator_1_MethodAsync__1.htm)|
Регистрирует метод, который можно асинхронно выполнить для текущего типа
расширения.  
---|---  
##  __См. также
#### Ссылки
[Tessa.Extensions - пространство имён](N_Tessa_Extensions.htm)
