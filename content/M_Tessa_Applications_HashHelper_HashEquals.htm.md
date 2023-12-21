# HashHelper.HashEquals - метод
Сравнивает контрольные суммы
## __Definition
 **Пространство имён:** [Tessa.Applications](N_Tessa_Applications.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static bool HashEquals(
    	[CanBeNullAttribute] byte[] sourceHash,
    	[CanBeNullAttribute] byte[] comparedHash
    )
VB __Копировать
     Public Shared Function HashEquals ( 
    	<CanBeNullAttribute> sourceHash As Byte(),
    	<CanBeNullAttribute> comparedHash As Byte()
    ) As Boolean
C++ __Копировать
     public:
    static bool HashEquals(
    	[CanBeNullAttribute] array<unsigned char>^ sourceHash, 
    	[CanBeNullAttribute] array<unsigned char>^ comparedHash
    )
F# __Копировать
     static member HashEquals : 
            [<CanBeNullAttribute>] sourceHash : byte[] * 
            [<CanBeNullAttribute>] comparedHash : byte[] -> bool 
#### Параметры
sourceHash [Byte](https://learn.microsoft.com/dotnet/api/system.byte)[]
     Исходная контрольная сумма 
comparedHash [Byte](https://learn.microsoft.com/dotnet/api/system.byte)[]
     Сравниваемая контрольная сумма 
#### Возвращаемое значение
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)  
Результат сравнения
## __См. также
#### Ссылки
[HashHelper - ](T_Tessa_Applications_HashHelper.htm)
[Tessa.Applications - пространство имён](N_Tessa_Applications.htm)
