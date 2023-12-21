# DataProtectionServiceExtender.Unprotect - метод
Осуществляет шифрование строки данных data
##  __Definition
 **Пространство имён:** [Tessa.Applications](N_Tessa_Applications.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    [CanBeNullAttribute]
    public static string Unprotect(
    	[NotNullAttribute] this IDataProtectionService dataProtectionService,
    	[CanBeNullAttribute] string data
    )
VB __Копировать
    <ExtensionAttribute>
    <CanBeNullAttribute>
    Public Shared Function Unprotect ( 
    	<NotNullAttribute> dataProtectionService As IDataProtectionService,
    	<CanBeNullAttribute> data As String
    ) As String
C++ __Копировать
     public:
    [ExtensionAttribute]
    [CanBeNullAttribute]
    static String^ Unprotect(
    	[NotNullAttribute] IDataProtectionService^ dataProtectionService, 
    	[CanBeNullAttribute] String^ data
    )
F# __Копировать
     [<ExtensionAttribute>]
    [<CanBeNullAttribute>]
    static member Unprotect : 
            [<NotNullAttribute>] dataProtectionService : IDataProtectionService * 
            [<CanBeNullAttribute>] data : string -> string 
#### Параметры
dataProtectionService
[IDataProtectionService](T_Tessa_Applications_IDataProtectionService.htm)
     Сервис шифрования данных 
data [String](https://learn.microsoft.com/dotnet/api/system.string)
     Шифруемые данные 
#### Возвращаемое значение
[String](https://learn.microsoft.com/dotnet/api/system.string)  
Зашифрованные данные в виде строки или null
#### Примечание об использовании
В Visual Basic и C# этот метод можно вызывать как метод экземпляра для любого
объекта типа
[IDataProtectionService](T_Tessa_Applications_IDataProtectionService.htm). При
вызове метода для экземпляра следует опускать первый параметр. Дополнительные
сведения см. в разделе [Методы расширения (Visual
Basic)](https://docs.microsoft.com/dotnet/visual-basic/programming-
guide/language-features/procedures/extension-methods) или [Методы расширения
(Руководство по программированию в
C#)](https://docs.microsoft.com/dotnet/csharp/programming-guide/classes-and-
structs/extension-methods).
##  __См. также
#### Ссылки
[DataProtectionServiceExtender -
](T_Tessa_Applications_DataProtectionServiceExtender.htm)
[Tessa.Applications - пространство имён](N_Tessa_Applications.htm)
