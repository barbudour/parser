# DocumentNumberDirector.GetPlaceholderDateTimeUtc - метод
##  __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Numbers](N_Tessa_Extensions_Default_Shared_Numbers.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     protected override DateTime GetPlaceholderDateTimeUtc(
    	string placeholder,
    	INumberContext context,
    	NumberTypeDescriptor numberType,
    	string formatString,
    	long? number = null
    )
VB __Копировать
     Protected Overrides Function GetPlaceholderDateTimeUtc ( 
    	placeholder As String,
    	context As INumberContext,
    	numberType As NumberTypeDescriptor,
    	formatString As String,
    	Optional number As Long? = Nothing
    ) As DateTime
C++ __Копировать
     protected:
    virtual DateTime GetPlaceholderDateTimeUtc(
    	String^ placeholder, 
    	INumberContext^ context, 
    	NumberTypeDescriptor^ numberType, 
    	String^ formatString, 
    	Nullable<long long> number = nullptr
    ) override
F# __Копировать
     abstract GetPlaceholderDateTimeUtc : 
            placeholder : string * 
            context : INumberContext * 
            numberType : NumberTypeDescriptor * 
            formatString : string * 
            ?number : Nullable<int64> 
    (* Defaults:
            let _number = defaultArg number null
    *)
    -> DateTime 
    override GetPlaceholderDateTimeUtc : 
            placeholder : string * 
            context : INumberContext * 
            numberType : NumberTypeDescriptor * 
            formatString : string * 
            ?number : Nullable<int64> 
    (* Defaults:
            let _number = defaultArg number null
    *)
    -> DateTime 
#### Параметры
placeholder [String](https://learn.microsoft.com/dotnet/api/system.string)
context [INumberContext](T_Tessa_Cards_Numbers_INumberContext.htm)
numberType
[NumberTypeDescriptor](T_Tessa_Cards_Numbers_NumberTypeDescriptor.htm)
formatString [String](https://learn.microsoft.com/dotnet/api/system.string)
number
[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[Int64](https://learn.microsoft.com/dotnet/api/system.int64)>
(Optional)
#### Возвращаемое значение
[DateTime](https://learn.microsoft.com/dotnet/api/system.datetime)
##  __См. также
#### Ссылки
[DocumentNumberDirector -
](T_Tessa_Extensions_Default_Shared_Numbers_DocumentNumberDirector.htm)
[Tessa.Extensions.Default.Shared.Numbers - пространство
имён](N_Tessa_Extensions_Default_Shared_Numbers.htm)
