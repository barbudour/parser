# GenericExtensions.OnNullThrow<TValue, TException> \- метод
Возвращает значение параметра value, если он не равен null, в противном случае
вызывает исключение exception
##  __Definition
 **Пространство имён:** [Tessa.Applications](N_Tessa_Applications.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    [NotNullAttribute]
    public static TValue OnNullThrow<TValue, TException>(
    	[CanBeNullAttribute] this TValue value,
    	[NotNullAttribute] TException exception
    )
    where TValue : class
    where TException : new(), Exception
VB __Копировать
    <ExtensionAttribute>
    <NotNullAttribute>
    Public Shared Function OnNullThrow(Of TValue As Class, TException As {New, Exception}) ( 
    	<CanBeNullAttribute> value As TValue,
    	<NotNullAttribute> exception As TException
    ) As TValue
C++ __Копировать
     public:
    [ExtensionAttribute]
    [NotNullAttribute]
    generic<typename TValue, typename TException>
    where TValue : ref class
    where TException : gcnew(), Exception
    static TValue OnNullThrow(
    	[CanBeNullAttribute] TValue value, 
    	[NotNullAttribute] TException exception
    )
F# __Копировать
     [<ExtensionAttribute>]
    [<NotNullAttribute>]
    static member OnNullThrow : 
            [<CanBeNullAttribute>] value : 'TValue * 
            [<NotNullAttribute>] exception : 'TException -> 'TValue  when 'TValue : not struct when 'TException : new() and Exception
#### Параметры
value TValue
     Значение параметра 
exception TException
     Исключение 
#### Параметры типа
TValue
     Тип параметра 
TException
     Тип исключения 
#### Возвращаемое значение
TValue  
Значение параметра value
#### Примечание об использовании
В Visual Basic и C# этот метод можно вызывать как метод экземпляра для любого
объекта типа TValue. При вызове метода для экземпляра следует опускать первый
параметр. Дополнительные сведения см. в разделе [Методы расширения (Visual
Basic)](https://docs.microsoft.com/dotnet/visual-basic/programming-
guide/language-features/procedures/extension-methods) или [Методы расширения
(Руководство по программированию в
C#)](https://docs.microsoft.com/dotnet/csharp/programming-guide/classes-and-
structs/extension-methods).
##  __См. также
#### Ссылки
[GenericExtensions - ](T_Tessa_Applications_GenericExtensions.htm)
[Tessa.Applications - пространство имён](N_Tessa_Applications.htm)
