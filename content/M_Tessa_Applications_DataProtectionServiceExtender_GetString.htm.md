# DataProtectionServiceExtender.GetString - метод
Преобразует массив байт bytes в строку
## __Definition
 **Пространство имён:** [Tessa.Applications](N_Tessa_Applications.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    [NotNullAttribute]
    public static string GetString(
    	[NotNullAttribute] byte[] bytes
    )
VB __Копировать
    <NotNullAttribute>
    Public Shared Function GetString ( 
    	<NotNullAttribute> bytes As Byte()
    ) As String
C++ __Копировать
     public:
    [NotNullAttribute]
    static String^ GetString(
    	[NotNullAttribute] array<unsigned char>^ bytes
    )
F# __Копировать
     [<NotNullAttribute>]
    static member GetString : 
            [<NotNullAttribute>] bytes : byte[] -> string 
#### Параметры
bytes [Byte](https://learn.microsoft.com/dotnet/api/system.byte)[]
     Массив байт 
#### Возвращаемое значение
[String](https://learn.microsoft.com/dotnet/api/system.string)  
Строка полученная из массива байт
## __См. также
#### Ссылки
[DataProtectionServiceExtender -
](T_Tessa_Applications_DataProtectionServiceExtender.htm)
[Tessa.Applications - пространство имён](N_Tessa_Applications.htm)
