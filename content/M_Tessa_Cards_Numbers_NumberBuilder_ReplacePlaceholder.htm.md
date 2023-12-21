# NumberBuilder.ReplacePlaceholder - метод
Заменяет плейсхолдеры в строке для форматирования номера или имени
последовательности и возвращает строку, содержащую заменённый плейсхолдер или
null, если плейсхолдер заменить не удалось. Неизвестные плейсхолдеры не
изменяются в результирующей строке номера.
## __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected virtual string ReplacePlaceholder(
    	string placeholder,
    	INumberContext context,
    	NumberTypeDescriptor numberType,
    	string formatString,
    	long? number = null
    )
VB __Копировать
     Protected Overridable Function ReplacePlaceholder ( 
    	placeholder As String,
    	context As INumberContext,
    	numberType As NumberTypeDescriptor,
    	formatString As String,
    	Optional number As Long? = Nothing
    ) As String
C++ __Копировать
     protected:
    virtual String^ ReplacePlaceholder(
    	String^ placeholder, 
    	INumberContext^ context, 
    	NumberTypeDescriptor^ numberType, 
    	String^ formatString, 
    	Nullable<long long> number = nullptr
    )
F# __Копировать
     abstract ReplacePlaceholder : 
            placeholder : string * 
            context : INumberContext * 
            numberType : NumberTypeDescriptor * 
            formatString : string * 
            ?number : Nullable<int64> 
    (* Defaults:
            let _number = defaultArg number null
    *)
    -> string 
    override ReplacePlaceholder : 
            placeholder : string * 
            context : INumberContext * 
            numberType : NumberTypeDescriptor * 
            formatString : string * 
            ?number : Nullable<int64> 
    (* Defaults:
            let _number = defaultArg number null
    *)
    -> string 
#### Параметры
placeholder [String](https://learn.microsoft.com/dotnet/api/system.string)
     Плейсхолдер без обрамляющих фигурных скобок, который требуется заменить. Чувствителен к регистру. 
context [INumberContext](T_Tessa_Cards_Numbers_INumberContext.htm)
    Контекст события, происходящего с номером.
numberType
[NumberTypeDescriptor](T_Tessa_Cards_Numbers_NumberTypeDescriptor.htm)
    Тип номера.
formatString [String](https://learn.microsoft.com/dotnet/api/system.string)
     Строка форматирования, в которой содержится заданный плейсхолдер placeholder. 
number
[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[Int64](https://learn.microsoft.com/dotnet/api/system.int64)>
(Optional)
     Форматируемый номер в его числовом представлении или null, если форматируется не номер, а имя последовательности. 
#### Возвращаемое значение
[String](https://learn.microsoft.com/dotnet/api/system.string)  
Строка, заменяющая плейсхолдер placeholder, или null, если заменить
плейсхолдер не удалось.
## __См. также
#### Ссылки
[NumberBuilder - ](T_Tessa_Cards_Numbers_NumberBuilder.htm)
[Tessa.Cards.Numbers - пространство имён](N_Tessa_Cards_Numbers.htm)
