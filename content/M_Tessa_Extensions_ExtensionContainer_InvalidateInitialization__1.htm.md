# ExtensionContainer.InvalidateInitialization<TExtension> \- метод
Принудительно устанавливает необходимость повторного выполнения этапов
инициализации и упорядочивания для заданного типа расширения. Вызывать метод
не требуется в случае, если была повторно зарегистрирована стратегия
инициализации.
## __Definition
 **Пространство имён:** [Tessa.Extensions](N_Tessa_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public void InvalidateInitialization<TExtension>()
    where TExtension : class, IExtension
VB __Копировать
     Public Sub InvalidateInitialization(Of TExtension As {Class, IExtension})
C++ __Копировать
     public:
    generic<typename TExtension>
    where TExtension : ref class, IExtension
    virtual void InvalidateInitialization() sealed
F# __Копировать
     abstract InvalidateInitialization : unit -> unit  when 'TExtension : not struct and IExtension
    override InvalidateInitialization : unit -> unit  when 'TExtension : not struct and IExtension
#### Параметры типа
TExtension
    Тип расширения.
#### Реализации
[IExtensionContainer.InvalidateInitialization<TExtension>()](M_Tessa_Extensions_IExtensionContainer_InvalidateInitialization__1.htm)  
##  __См. также
#### Ссылки
[ExtensionContainer - ](T_Tessa_Extensions_ExtensionContainer.htm)
[Tessa.Extensions - пространство имён](N_Tessa_Extensions.htm)
