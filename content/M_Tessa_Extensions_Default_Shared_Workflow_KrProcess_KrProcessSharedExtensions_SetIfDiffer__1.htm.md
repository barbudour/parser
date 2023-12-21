# KrProcessSharedExtensions.SetIfDiffer<T> \- метод
Задаёт новое значение полю key в контейнере полей секции aci, если оно было
изменено.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.KrProcess](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public static bool SetIfDiffer<T>(
    	this ICardFieldContainer aci,
    	string key,
    	T value
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function SetIfDiffer(Of T) ( 
    	aci As ICardFieldContainer,
    	key As String,
    	value As T
    ) As Boolean
C++ __Копировать
     public:
    [ExtensionAttribute]
    generic<typename T>
    static bool SetIfDiffer(
    	ICardFieldContainer^ aci, 
    	String^ key, 
    	T value
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member SetIfDiffer : 
            aci : ICardFieldContainer * 
            key : string * 
            value : 'T -> bool 
#### Параметры
aci [ICardFieldContainer](T_Tessa_Cards_ICardFieldContainer.htm)
    Объект, являющийся контейнером для полей карточки.
key [String](https://learn.microsoft.com/dotnet/api/system.string)
    Имя поля.
value T
    Новое значение.
#### Параметры типа
T
    Тип значения.
#### Возвращаемое значение
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)  
Значение true, если новое значение было записано в поле, иначе - false.
#### Примечание об использовании
В Visual Basic и C# этот метод можно вызывать как метод экземпляра для любого
объекта типа [ICardFieldContainer](T_Tessa_Cards_ICardFieldContainer.htm). При
вызове метода для экземпляра следует опускать первый параметр. Дополнительные
сведения см. в разделе [Методы расширения (Visual
Basic)](https://docs.microsoft.com/dotnet/visual-basic/programming-
guide/language-features/procedures/extension-methods) или [Методы расширения
(Руководство по программированию в
C#)](https://docs.microsoft.com/dotnet/csharp/programming-guide/classes-and-
structs/extension-methods).
##  __См. также
#### Ссылки
[KrProcessSharedExtensions -
](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions.htm)
[Tessa.Extensions.Default.Shared.Workflow.KrProcess - пространство
имён](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess.htm)
