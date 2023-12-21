# IExtensionContainer.InvalidateInitialization<TExtension> \- метод
Принудительно устанавливает необходимость повторного выполнения этапов
инициализации и упорядочивания для заданного типа расширения. Вызывать метод
не требуется в случае, если была повторно зарегистрирована стратегия
инициализации.
## __Definition
 **Пространство имён:** [Tessa.Extensions](N_Tessa_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     void InvalidateInitialization<TExtension>()
    where TExtension : class, IExtension
VB __Копировать
     Sub InvalidateInitialization(Of TExtension As {Class, IExtension})
C++ __Копировать
    generic<typename TExtension>
    where TExtension : ref class, IExtension
    void InvalidateInitialization()
F# __Копировать
     abstract InvalidateInitialization : unit -> unit  when 'TExtension : not struct and IExtension
#### Параметры типа
TExtension
    Тип расширения.
##  __См. также
#### Ссылки
[IExtensionContainer - ](T_Tessa_Extensions_IExtensionContainer.htm)
[Tessa.Extensions - пространство имён](N_Tessa_Extensions.htm)
